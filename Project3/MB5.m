function [liklihood,P,Q] = MB5(data, beta, alphap, alphai, alpha_inv, k,p)
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
    P = exp(beta*Q)./sum(exp(beta*Q),2);
    QD = Qd;
    last_was_private = 0;
    liklihood = 0;
    for i = 1:length(trial)
       if ~(ID(i)=="dem")%is not a demonstrating trial
           c = str2double(choice(i))+1;
           if c == 1
                  cn = 2;
           else
                  cn = 1;
           end
           Qd = Q;
           P(state(i),:) = exp(beta*Qd(state(i),:))./sum(exp(beta*Qd(state(i),:)));
           [~,d] =max(QD(state(i),:));
           if d == 1
               dn = 2;
           else
               dn = 1;
           end
           Qd(state(i),d) = Qd(state(i),d) + alphai*(1-Qd(state(i),d));
           if last_choice(state(i))>0
               Qd(state(i),c) = Qd(state(i),c) + p;
           end
           P(state(i),:) = exp(beta*P(state(i),:))./sum(exp(beta*P(state(i),:)));
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
           QD(state(i),d) = QD(state(i),d) + alpha_inv*(1-QD(state(i),d));
       end
    end
end