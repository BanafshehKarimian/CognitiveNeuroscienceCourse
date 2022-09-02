function [liklihood,P,Q] = DB1(data, beta, alpha_rpe, alpha_sape, alpha_inv, k,p)
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
    Qd = Q;
    history_choice = [];
    last_was_private = 0;
    liklihood = 0;
    P = softmax(beta*Q')';
    for i = 1:length(trial)
       if ~(ID(i)=="dem")%is not a demonstrating trial
           c = str2double(choice(i))+1;
           liklihood = liklihood - log(P(state(i),c));
           if c == 1
                  cn = 2;
           else
                  cn = 1;
           end
           RPE =  str2double(reward{i}) - Q(state(i),c);
           Q(state(i),c) = Q(state(i),c) + alpha_rpe * RPE;
           RPE =  -1*str2double(reward{i}) - Q(state(i),cn);
           Q(state(i),cn) = Q(state(i),cn) + alpha_rpe * RPE;
           Qd = Q;
           Qd(state(i),c) = Qd(state(i),c) + p;
           P(state(i),:) = softmax(beta*Qd(state(i),:)')';
           last_choice(state(i)) = c;
       else
           P(state(i),:) = softmax(beta*Qd(state(i),:)')';
           d = demonstrator(i)+1;
           if d == 1
               dn = 2;
           else
               dn = 1;
           end
           P(state(i),d) = P(state(i),d) + alpha_sape*(1-P(state(i),d));
           P(state(i),dn) = 1 - P(state(i),d);
       end
    end
end