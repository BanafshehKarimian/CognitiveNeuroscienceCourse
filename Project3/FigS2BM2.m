data = readtable('task2.csv');
beta = 0.4;
alpha_rpe = 0.1;
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
logEvidenceSK = zeros(4,length(id));
% generate data
% -------------------------------------------------------------------------
alpha_rpe = 0.2;
alpha_sape = 0.1;
for j = 1 : length(id)
    i = id(j);
    % compute model evidence (frequentist limit)
    datasbj = data(data.expid == i, :);
    [liklihood2,P2,Q2] = BM2(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood1,P1,Q1] = BM1(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    demonstrator = table2array(datasbj(:,5));
    demonstrator = table2array(datasbj(:,3));
    if demonstrator(i) == "skilled.dem"
        logEvidenceSK(1,j) = liklihood1;
        logEvidenceSK(2,j) = liklihood2;
    else
        logEvidenceUN(1,j) = liklihood1;
        logEvidenceUN(2,j) = liklihood2;
    end
end
options.verbose = false;
[p2, o2] = VBA_groupBMC (logEvidenceUN(any(logEvidenceUN,2),:), options);
set (o2.options.handles.hf, 'name', 'unskilled')
[p2, o2] = VBA_groupBMC (logEvidenceSK(any(logEvidenceSK,2),:), options);
set (o2.options.handles.hf, 'name', 'skilled')