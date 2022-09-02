function [liklihood,P,Q] = BM1(data, beta, alphap, alphai, alpha_inv, k,p)
    state = table2array(data(:,7));%state (i.e., pair of symbols) state (i.e., pair of cue)
    stateCnt = length(state);
    reward = table2array(data(:,15));
    choice = table2array(data(:,14));
    ID = table2array(data(:,2));
    trial = table2array(data(:,4));
    cond_demonstrator = table2array(data(:,5));
    demonstrator = table2array(data(:,12));
    cond_obs = table2array(data(:,5));
    %hyper parameters:
    last_choice = zeros(stateCnt);
    Q = zeros(stateCnt,2);
    history_choice = [];
    P = [0,0];
    liklihood = 0;
    for i = 1:length(trial)
       if ~(ID(i)=="dem")%is not a demonstrating trial
           Qd = Q;
           P = softmax(beta*Qd')';
           if last_choice(state(i))>0
               Qd(state(i),c) = Qd(state(i),c) + p;
           end
           c = str2double(choice(i))+1;
           if c == 1
                  cn = 2;
           else
                  cn = 1;
           end
           liklihood = liklihood - log(P(state(i),c));
           RPE =  str2double(reward{i}) - Q(state(i),c);
           Q(state(i),c) = Q(state(i),c) + alphap * RPE;
           last_choice(state(i)) = c;
       end
    end
end