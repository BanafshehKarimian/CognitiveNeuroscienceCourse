data = readtable('task1.csv');
beta = 4;
alpha_rpe = 0.2;
alpha_sape = 0.1;
alpha_inv = 0.1;
k = 0.01;
p = 10;
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
alpha_rpe = 0.2;
alpha_sape = 0.1;
for j = 1 : length(id)
    i = id(j);
    % compute model evidence (frequentist limit)
    datasbj = data(data.expid == i, :);
    [liklihood2,PBM2,QBM2] = MetaVS(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood1,PBM1,QBM1] = VS2(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    demonstrator = table2array(datasbj(:,5));
        logEvidence(1,j) = liklihood1;
        logEvidence(2,j) = liklihood2;
end
options.verbose = false;
[p2, o2] = VBA_groupBMC (logEvidence(any(logEvidence,2),:), options);
set (o2.options.handles.hf, 'name', 'exp1')
data = readtable('task2.csv');
id = str2double(unique(table2array(data(:,2))));
id = id(1:length(id)-1);
logEvidence = zeros(4,length(id));
for j = 1 : length(id)
    i = id(j);
    % compute model evidence (frequentist limit)
    datasbj = data(data.expid == i, :);
    demonstrator = table2array(datasbj(:,3));
    [liklihood2,PBM2,QBM2] = MetaVS(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood1,PBM1,QBM1] = VS2(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    demonstrator = table2array(datasbj(:,3));
    logEvidence(1,j) = liklihood1;
    logEvidence(2,j) = liklihood2;
end
[p2, o2] = VBA_groupBMC (logEvidence(any(logEvidence,2),:), options);
set (o2.options.handles.hf, 'name', 'exp2')