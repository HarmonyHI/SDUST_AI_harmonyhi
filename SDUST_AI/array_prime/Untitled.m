n = input('�����ж�����ĳ���');
node = zeros(1,n);
for i=1:n
    node(i) = input(sprintf('�����������%d������',i));
end
ans1 = zeros(1,n);
i = 1;
for item=node
    ans1(i) = judge(item);
    i = i + 1;
end
disp(ans1);
