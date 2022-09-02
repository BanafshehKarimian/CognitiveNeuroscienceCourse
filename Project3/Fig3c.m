beta = 0.4;
alpha_inv = 0.1;
k = 0.01;
p=1;
x0 = [0.1,0.1]
task1SKi = [];
task1UNi = [];
task1SKp = [];
task1UNp = [];
task1SK = [];
task1UN = [];
task2UN = [];
task2SK = [];
alpha_rpe = 0.2;
alpha_sape = 0.1;
data = readtable('task1.csv');
id = str2double(unique(table2array(data(:,2))));
id = id(1:length(id)-1);
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
    
    fun = @(x)f(x, datasbj, beta, alpha_inv, k,p);
    x = fmincon(fun,x0,[],[], [],[],[0.001,0.001],[0.99,0.99]);
    task1UN = [task1UN,x(1)]
    
end
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
    
    fun = @(x)f(x, datasbj, beta, alpha_inv, k,p);
    x = fmincon(fun,x0,[],[], [],[],[0.001,0.001],[0.99,0.99]);
    task1SK = [task1SK,x(1)]
    
end
violinplot([task1UN;task1SK]')
figure
beta = 0.4;
alpha_inv = 0.1;
k = 0.01;
p=1;
x0 = [0.1,0.1]
data = readtable('task2.csv');
id = str2double(unique(table2array(data(:,2))));
id = id(1:length(id)-1);
x0 = [0.1,0.1];
p=10;
for j = 1 : length(id)
    i = id(j);
    % compute model evidence (frequentist limit)
    datasbj = data(data.expid == i, :);
    demonstrator = table2array(datasbj(:,3));
    fun = @(x)f(x, datasbj, beta, alpha_inv, k,p);
    if demonstrator(1) == "skilled.dem"
            beta = 10;
            x = fmincon(fun,x0,[1 0],1, [],[],[0.01,0.01],[0.99,0.99]);
            task1SKi = [task1SKi, x(1)]
            task1SKp = [task1SKp, x(2)]
    else
            beta = 10;
            x = fmincon(fun,x0,[1 0],1, [],[],[0.01,0.01],[0.99,0.99]);
            task1UNi = [task1UNi, x(1)]
            task1UNp = [task1UNp, x(2)]
    end
end
violinplot([task1UNi;task1SKi]')
function liklihood = f(inp, data, beta, alpha_inv, k,p)
    alphai = inp(1);
    alphap = inp(2);
    [liklihood,P,Q] = VS1(data, beta, alphap, alphai, alpha_inv, k,p);
end