N = 1000;
r =  [1:N];
r = r/10;
for It = 1:length(r)
    I = r(It)
    [t,y] = ode45(@(t,x)MorisLecar(t,x,I),[0 0.4],[-66; 0]);
    [t2,y2] = ode45(@(t,x)MorisLecar(t,x,0),[0.4 100],[y(end,1); y(end,2)]);
    y = [y;y2];
    t = [t;t2];
    if max(y(:,1)) > 0
        if max(y(:,2))>0
           break 
        end
    end

end
I
I = I - 0.1;
    [t,y] = ode45(@(t,x)MorisLecar(t,x,I),[0 0.4],[-66; 0]);
    [t2,y2] = ode45(@(t,x)MorisLecar(t,x,0),[0.4 100],[y(end,1); y(end,2)]);
    y = [y;y2];
    t = [t;t2];
subplot(3,2,1)
plot(t,y(:,1))
title("V for I = "+num2str(I))
subplot(3,2,2)
plot(t,y(:,2))
title("n for I = "+num2str(I))
I =  I + 0.1;
    [t,y] = ode45(@(t,x)MorisLecar(t,x,I),[0 0.4],[-66; 0]);
    [t2,y2] = ode45(@(t,x)MorisLecar(t,x,0),[0.4 100],[y(end,1); y(end,2)]);
    y = [y;y2];
    t = [t;t2];
subplot(3,2,3)
plot(t,y(:,1))
title("V for I =  "+num2str(I))
subplot(3,2,4)
plot(t,y(:,2))
title("n for I ="+num2str(I))
I =  I+10;
    [t,y] = ode45(@(t,x)MorisLecar(t,x,I),[0 0.4],[-66; 0]);
    [t2,y2] = ode45(@(t,x)MorisLecar(t,x,0),[0.4 100],[y(end,1); y(end,2)]);
    y = [y;y2];
    t = [t;t2];
subplot(3,2,5)
plot(t,y(:,1))
title("V for I ="+num2str(I))
subplot(3,2,6)
plot(t,y(:,2))
title("n for I ="+num2str(I))
