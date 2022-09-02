data = readtable('task1.csv');
beta = 2;
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
logEvidence = zeros(3,length(id));
logEvidenceUN = zeros(3,length(id));
logEvidenceSK = zeros(2,length(id));
% generate data
% -------------------------------------------------------------------------
alpha_rpe = 0.1;
alpha_sape = 0.01;
for j = 1 : length(id)
    i = id(j);
    % compute model evidence (frequentist limit)
    datasbj = data(data.expid == i, :);
    [liklihood1,PBM2,QBM2] = MB1(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood2,PBM1,QBM1] = MB2(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood3,PBM1,QBM1] = MB3(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood4,PBM1,QBM1] = MB4(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood5,PBM1,QBM1] = MB5(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood6,PBM1,QBM1] = MB6(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood7,PBM1,QBM1] = MB7(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood8,PBM1,QBM1] = MB8(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood9,PBM1,QBM1] = MB9(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    logEvidence(1,j) = liklihood1;
    logEvidence(2,j) = liklihood2;
    logEvidence(3,j) = liklihood3;
    logEvidence(4,j) = liklihood4;
    logEvidence(5,j) = liklihood5;
    logEvidence(6,j) = liklihood6;
    logEvidence(7,j) = liklihood7;
    logEvidence(8,j) = liklihood8;
    logEvidence(9,j) = liklihood9;
end
alpha_rpe = 0.2;
alpha_sape = 0.05;
for j = 1 : length(id)
    i = id(j);
    % compute model evidence (frequentist limit)
    datasbj = data(data.expid == i, :);
    ind = min(find(table2array(datasbj(:,5)) == "skilled.dem"));
    datasbj = datasbj(1:ind-1,:);
    %datasbj = datasbj(find(table2array(datasbj(:,5)) == "unskilled.dem"),:);
    if size(datasbj)==0
        continue
    end
    [liklihood1,PBM2,QBM2] = MB1(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood2,PBM1,QBM1] = MB2(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood3,PBM1,QBM1] = MB3(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood4,PBM1,QBM1] = MB4(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood5,PBM1,QBM1] = MB5(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood6,PBM1,QBM1] = MB6(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood7,PBM1,QBM1] = MB7(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood8,PBM1,QBM1] = MB8(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood9,PBM1,QBM1] = MB9(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    logEvidenceUN(1,j) = liklihood1;
    logEvidenceUN(2,j) = liklihood2;
    logEvidenceUN(3,j) = liklihood3;
    logEvidenceUN(4,j) = liklihood4;
    logEvidenceUN(5,j) = liklihood5;
    logEvidenceUN(6,j) = liklihood6;
    logEvidenceUN(7,j) = liklihood7;
    logEvidenceUN(8,j) = liklihood8;
    logEvidenceUN(9,j) = liklihood9;
end
alpha_rpe = 0.2;
alpha_sape = 0.1;
for j = 1 : length(id)
    i = id(j);
    % compute model evidence (frequentist limit)
    datasbj = data(data.expid == i, :);
    ind = min(find(table2array(datasbj(:,5)) == "unskilled.dem"));
    datasbj = datasbj(1:ind-1,:);
    %datasbj = datasbj(find(table2array(datasbj(:,5)) == "skilled.dem"),:);
    if size(datasbj)==0
        continue
    end

    [liklihood1,PBM2,QBM2] = MB1(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood2,PBM1,QBM1] = MB2(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood3,PBM1,QBM1] = MB3(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood4,PBM1,QBM1] = MB4(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood5,PBM1,QBM1] = MB5(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood6,PBM1,QBM1] = MB6(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood7,PBM1,QBM1] = MB7(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood8,PBM1,QBM1] = MB8(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    [liklihood9,PBM1,QBM1] = MB9(datasbj, beta, alpha_rpe, alpha_sape, alpha_inv, k,p);
    logEvidenceSK(1,j) = liklihood6;
    logEvidenceSK(2,j) = liklihood9;
    logEvidenceSK(3,j) = liklihood9;
    logEvidenceSK(4,j) = liklihood4;
    logEvidenceSK(5,j) = liklihood5;
    logEvidenceSK(6,j) = liklihood6;
    logEvidenceSK(7,j) = liklihood7;
    logEvidenceSK(8,j) = liklihood8;
    logEvidenceSK(9,j) = liklihood9;
end
options.verbose = false;
[p2, o2] = VBA_groupBMC (logEvidence(any(logEvidence,2),:), options);
set (o2.options.handles.hf, 'name', 'unskilled & skilled')
[p2, o2] = VBA_groupBMC (logEvidenceUN(any(logEvidenceUN,2),:), options);
set (o2.options.handles.hf, 'name', 'unskilled')
[p2, o2] = VBA_groupBMC (logEvidenceSK(any(logEvidenceSK,2),:), options);
set (o2.options.handles.hf, 'name', 'skilled')