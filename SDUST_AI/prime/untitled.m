function[]=untitled()
    while true
        n=input('');
        if(n==0)
            break;
        end
        if isprime(n)
            fprintf("%d\n",n);
        end
    end
end