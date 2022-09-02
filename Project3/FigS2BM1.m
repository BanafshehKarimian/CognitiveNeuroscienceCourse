data = readtable('task1.csv');
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
logEvidence = zeros(4,length(id));
logEvidenceUN = zeros(4,length(id));
logEvidenceSK = zeros(4,length(id));
% generate data
% -------------------------------------------------------------------------
alpha_rpe = 0.1;
alpha_sape = 0.01;
for j = 1 : length(id)
    i = id(j);
    % compute model evidence (frequentist limit)
    datasbj = data(data.expid == i, :);
    [liklihoodBM2,PBM2,QBM2] = BM2(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihoodBM1,PBM1,QBM1] = BM1(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    demonstrator = table2array(datasbj(:,5));
        logEvidence(1,j) = liklihoodBM1;
        logEvidence(2,j) = liklihoodBM2;
end
alpha_rpe = 0.2;
alpha_sape = 0.05;
for j = 1 : length(id)
    i = id(j);
    % compute model evidence (frequentist limit)
    datasbj = data(data.expid == i, :);
    ind = min(find(table2array(datasbj(:,5)) == "skilled.dem"));
    %datasbj = datasbj(1:ind-1,:);
    datasbj = datasbj(find(table2array(datasbj(:,5)) == "unskilled.dem"),:);
    if size(datasbj)==0
        continue
    end
    [liklihoodBM2,PBM2,QBM2] = BM2(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihoodBM1,PBM1,QBM1] = BM1(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    demonstrator = table2array(datasbj(:,5));
        logEvidenceUN(1,j) = liklihoodBM1;
        logEvidenceUN(2,j) = liklihoodBM2;
end
alpha_rpe = 0.2;
alpha_sape = 0.1;
for j = 1 : length(id)
    i = id(j);
    % compute model evidence (frequentist limit)
    datasbj = data(data.expid == i, :);
    ind = min(find(table2array(datasbj(:,5)) == "unskilled.dem"));
    %datasbj = datasbj(1:ind-1,:);
    datasbj = datasbj(find(table2array(datasbj(:,5)) == "skilled.dem"),:);
    if size(datasbj)==0
        continue
    end
    [liklihoodBM2,PBM2,QBM2] = BM2(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihoodBM1,PBM1,QBM1] = BM1(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    demonstrator = table2array(datasbj(:,5));
        logEvidenceSK(1,j) = liklihoodBM1;
        logEvidenceSK(2,j) = liklihoodBM2;
end
options.verbose = false;
[p2, o2] = VBA_groupBMC (logEvidence(any(logEvidence,2),:), options);
set (o2.options.handles.hf, 'name', 'unskilled & skilled')
[p2, o2] = VBA_groupBMC (logEvidenceUN(any(logEvidenceUN,2),:), options);
set (o2.options.handles.hf, 'name', 'unskilled')
[p2, o2] = VBA_groupBMC (logEvidenceSK(any(logEvidenceSK,2),:), options);
set (o2.options.handles.hf, 'name', 'skilled')