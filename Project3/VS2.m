function [liklihood,P,Q] = VS2(data, beta, alphap, alphai, alpha_inv, k,p)
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
    last_was_private = 0;
    liklihood = 0;
    P = softmax(beta*Q')';
    for i = 1:length(trial)
       if ~(ID(i)=="dem")%is not a demonstrating trial
           c = str2double(choice(i))+1;
           if c == 1
                  cn = 2;
           else
                  cn = 1;
           end
           Qd = Q;
           if last_choice(state(i))>0
               Qd(state(i),c) = Qd(state(i),c) + p;
           end
           P(state(i),:) = softmax(beta*Qd(state(i),:)')';
           liklihood = liklihood - log(P(state(i),c));
           RPE =  str2double(reward{i}) - Q(state(i),c);
           Q(state(i),c) = Q(state(i),c) + alphap * RPE;
           RPE =  -1*str2double(reward{i}) - Q(state(i),cn);
           Q(state(i),cn) = Q(state(i),cn) + alphap * RPE;
           last_choice(state(i)) = c;
       else
           d = demonstrator(i)+1;
           if d == 1
               dn = 2;
           else
               dn = 1;
           end
           Q(state(i),d) = Q(state(i),d) + alphai*(1-Q(state(i),d));
           Q(state(i),dn) = Q(state(i),dn) + alphai*(-1-Q(state(i),dn));
       end
    end
end