const factorialDp = (n) => {
    // init the list
    target_list = [];
    target_list.push(1, 1);
    let result = 1;
    // Only loop if n is larger than 1, else return 1, or -1 if invalid
    if (n >= 2) {
        for (let i = 2; i <= n; i++) {
            let result = i * target_list[i - 1];
            target_list.push(result);
        };
        return target_list.pop();
    } else if (n < 0) {
        return -1;
    } else {
        return 1;
    }

};


const catalanNumbers = (n) => {
    // Catalan Numbers can be worked out as: (2n)! / ((n+1)!(n!))
    return (factorialDp(2 * n)) / ((factorialDp(n + 1)) * (factorialDp(n)))
};



const catalanDp = (n) => {
    // Catalan Numbers satisfy recurrence relations

    // C0 = 1 and Cn = ((2(2n-1))/(n+1)) * cn - 1

    // init the base case

    let arr = [1]

    // Loop for other cases if n > 0

    if (n == 0) {
        return 1;
    } else if (n < 0) {
        return -1;
    } else {
        for (i = 1; i <= n; i++) {
            let factor = ((2 * ((2 * i) - 1)) / (i + 1))
            arr.push(factor * arr[i - 1])

        }

        return arr;

    }
};
console.log(catalanDp(9))