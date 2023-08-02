n = input('输入判断数组的长度');
node = zeros(1,n);
for i=1:n
    node(i) = input(sprintf('你正在输入第%d个数字',i));
end
ans1 = zeros(1,n);
i = 1;
for item=node
    ans1(i) = judge(item);
    i = i + 1;
end
disp(ans1);
