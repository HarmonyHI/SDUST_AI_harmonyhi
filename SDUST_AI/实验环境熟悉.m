第一种方式
function[]=untitled()
    while true
        n=input("");
        if(n==0)
            break;
        end
        if isprime(n)
            fprintf("%d\n",n);
        end
    end
end
第二种方式
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
需要调用的自定义函数
function[is_ok] = judge(inpt)
    is_ok = false;
    if mod(inpt, 2) == 0
        is_ok = true;
    end
end

