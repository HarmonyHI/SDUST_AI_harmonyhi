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