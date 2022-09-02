data = readtable('task2.csv');
beta = [1,1,1,3];
alpha_rpe = 0.2;
alpha_sape = 0.1;
alpha_inv = 0.1;
k = 0.01;
p = 0;
% dimensions
% -------------------------------------------------------------------------
% number of subjects
id = str2double(unique(table2array(data(:,2))));
id = id(1:length(id)-1);
% number of observatiosn per subject
nObs = 64;
% number of predictors (regressors)
nPred = 4;
% parameters
% -------------------------------------------------------------------------
% noise variance
sigma2 = 1e0;
% signal strength
signal = 1e0; 
logEvidenceUN = zeros(4,length(id));
logEvidence = zeros(4,length(id));
% generate data
% -------------------------------------------------------------------------
for j = 1 : length(id)
    i = id(j);
    % compute model evidence (frequentist limit)
    datasbj = data(data.expid == i, :);
    [liklihoodBM2,PBM2,QBM2] = BM2(datasbj, beta(1), alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihoodDB4,PDB4,QDB4] = DB4(datasbj, beta(2), alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihoodMB9,PMB9,QMB9] = MB9(datasbj, beta(3), alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihoodVS1,PVS1,QVS1] = VS1(datasbj, beta(4), alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihoodBM1,PBM1,QBM1] = BM1(datasbj, beta(1), alpha_rpe, alpha_sape, alpha_inv, k,p);
    demonstrator = table2array(datasbj(:,3));
    if demonstrator(i) == "skilled.dem"
        logEvidence(1,j) = liklihoodBM2;
        logEvidence(2,j) = liklihoodDB4;
        logEvidence(3,j) = liklihoodMB9;
        logEvidence(4,j) = liklihoodVS1;
    else
        logEvidenceUN(1,j) = liklihoodBM2;
        logEvidenceUN(2,j) = liklihoodDB4;
        logEvidenceUN(3,j) = liklihoodMB9;
        logEvidenceUN(4,j) = liklihoodVS1;
    end
end
options.verbose = false;
[p2, o2] = VBA_groupBMC (logEvidence, options);
set (o2.options.handles.hf, 'name', 'skilled')
[p2, o2] = VBA_groupBMC (logEvidenceUN, options);
set (o2.options.handles.hf, 'name', 'unskilled')