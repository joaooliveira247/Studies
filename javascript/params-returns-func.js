// common
function sum(n1, n2) {
    n1 = isNaN(n1) ? 0 : n1;
    n2 = isNaN(n2) ? 0 : n2;
    return n1 + n2;
}

// es2015 default arg
function sum(n1=0, n2=0) {
    n1 = isNaN(n1) ? 0 : n1;
    n2 = isNaN(n2) ? 0 : n2;
    return n1 + n2;
}

// Optional
function calcSalary(salary, discount) {
    return salary - discount;
}