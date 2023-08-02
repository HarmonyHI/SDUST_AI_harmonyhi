x = linspace(0,1,20);
y = 2*x + 0.2*randn([1,20]);
pf = polyfit(x,y,1);
figure;plot(x,y,'o',x,polyval(pf,x))
