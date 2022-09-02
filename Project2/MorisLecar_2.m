N = 1000;
r =  [1:N];
r = r/100;
for It = 1:length(r)
    I = r(It)
    [t,y] = ode45(@(t,x)MorisLecar(t,x,I),[0 100],[-66; 0]);
    if max(y(:,1)) > 0
        if max(y(:,2))>0
           break 
        end
    end

end
I
I = I - 0.01;
[t,y] = ode45(@(t,x)MorisLecar(t,x,I),[0 100],[-66; 0]);
subplot(3,2,1)
plot(t,y(:,1))
title('V for I = 4.51')
subplot(3,2,2)
plot(t,y(:,2))
title('n for I = 4.51')
I =  I + 0.01;
[t,y] = ode45(@(t,x)MorisLecar(t,x,I),[0 100],[-66; 0]);
subplot(3,2,3)
plot(t,y(:,1))
title('V for I = 4.52')
subplot(3,2,4)
plot(t,y(:,2))
title('n for I = 4.52')
I =  4.7;
[t,y] = ode45(@(t,x)MorisLecar(t,x,I),[0 100],[-66; 0]);
subplot(3,2,5)
plot(t,y(:,1))
title('V for I = 4.7')
subplot(3,2,6)
plot(t,y(:,2))
title('n for I = 4.7')