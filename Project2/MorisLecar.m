function x = MorisLecar(t, x, I)
V = x(1);%-66;%potential
n = x(2);%0;%recovery
gL = 8;
gNa = 20;
gK = 10;
EL = -80;
ENa = 60;
EK = -90;
V1_2n = -25;
V1_2m = -20;
kn = 5;
km = 15;
Cm = 1;
tau = 1;
x = [dV(I,gL,V,EL,gK,n,EK,gNa,V1_2m,km,ENa,Cm); dn(V,V1_2n,kn,n,tau)]

function y = MV(x,V1_2m,km)
     y = 1+exp((V1_2m-x)/km);
     y = 1/y;
end
function y = NV(x,V1_2n,kn)
     y = 1+exp((V1_2n-x)/kn);
     y = 1/y;
end
function y = tauf(N)
     y = atanh(2*N-1)*1/2;
     y = 1/cosh(y);
end
function y = dV(I,gL,V,EL,gK,n,EK,gNa,V1_2m,km,ENa,Cm)
     y = I-gL*(V-EL)-gK*n*(V-EK)-gNa*MV(V,V1_2m,km)*(V-ENa);
     y = y/Cm;
end
function y = dn(V,V1_2n,kn,n, tau)
     y = NV(V,V1_2n,kn)-n;
     y = y/tau;%t(NV(V,V1_2n,kn));
end
end