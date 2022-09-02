beta = 0.4;
alpha_inv = 0.1;
k = 0.01;
p=1;
x0 = [0.1,0.1]
data = readtable('task1.csv');
id = str2double(unique(table2array(data(:,2))));
id = id(1:length(id)-1);
task1UNSKi = [];
task1UNSKp = [];
task1UNi = [];
task1UNp = [];
task1SKi = [];
task1SKp = [];
alpha_rpe = 0.2;
alpha_sape = 0.1;
for j = 1 : length(id)
    i = id(j);
    % compute model evidence (frequentist limit)
    datasbj = data(data.expid == i, :);
    fun = @(x)f(x, datasbj, beta, alpha_inv, k,p);
    x = fmincon(fun,x0,[],[],[],[],[0.01,0.01],[0.99,0.99]);
    task1UNSKi = [task1UNSKi, x(1)]
    task1UNSKp = [task1UNSKp, x(2)]
end
violinplot([task1UNSKp;task1UNSKi]')
figure
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
violinplot([task1UNp;task1UNi]')
figure
violinplot([task1SKp;task1SKi]')
function liklihood = f(inp, data, beta, alpha_inv, k,p)
    alphai = inp(1);
    alphap = inp(2);
    [liklihood,P,Q] = VS1(data, beta, alphap, alphai, alpha_inv, k,p);
end