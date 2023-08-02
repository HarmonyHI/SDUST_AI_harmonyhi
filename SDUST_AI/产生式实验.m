
q=input('smaller');
arr{1}.C = 'smaller';
arr{1}.T=q;
 

q=input('older than your mo/fa?');
arr{3}.C = 'isgrand';
arr{3}.T=q;

q=input('has long hair?');
arr{4}.C = 'iswoman';
arr{4}.T=q;

q=input('same fam?');
arr{5}.C = 'ismd';
arr{5}.T=q;

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
function [is_true] = op(arr, word)
    is_true=false;
    for iter=1:length(arr)
        if(strcmp(arr{iter}.C, word))
            if(arr{iter}.T == 1)
                is_true = true;
            end
        end
    end
end

    
 
