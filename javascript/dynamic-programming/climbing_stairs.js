/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    if (n == 1) {
        return 1
    };

    let current = 1 
    let previous = 1

    for (let i = 1; i < n; i ++) {
        let temp = current
        current = current+ previous
        previous = temp

    }
    return current
};

console.log(climbStairs(3))