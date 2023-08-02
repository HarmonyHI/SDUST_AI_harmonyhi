%¹æÔò¿â
% smaller? kids
% same with grandpa? -> dna/cust
% older than your mo/fa -> grand/nogrand
% has long hair -> man/woman
% 2 and 3 and same fam? -> md/uncle
q=input('smaller');
arr{1}.C = 'smaller';
arr{1}.T=q;
 

q=input('older than your mo/fa?');
arr{2}.C = 'isgrand';
arr{2}.T=q;

q=input('has long hair?');
arr{3}.C = 'iswoman';
arr{3}.T=q;

q=input('same fam?');
arr{4}.C = 'ismd';
arr{4}.T=q;

sum=1;
disp('ans£º')
while(1)
    sum=sum+1;
    if op(arr,'smaller')&&op(arr,'isgrand')
        disp('ÎÞ');
        break
    end
    if op(arr,'smaller')
        if op(arr, 'iswoman')
            disp('sister')
            break
        else
            disp('bro')
            break
        end
    end
        if op(arr, 'isgrand')
            if op(arr, 'iswoman')
                if op(arr, 'ismd')
                    continue
                else
                    disp('grandmom')
                    break
                end
            else
                if op(arr, 'ismd')
                    continue
                else
                    disp('grandpa')
                    break
                end
            end
        else
            if op(arr, 'iswoman')
                if op(arr, 'ismd')
                    disp('mom')
                    break
                else
                    disp('aunt')
                    break
                end
            else
                if op(arr, 'ismd')
                    disp('dad')
                    break
                else
                    disp('uncle')
                    break
                end
            end
        end
end
 