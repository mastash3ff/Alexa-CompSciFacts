
var oN = "big Oh of N";
var oN2 = "big Oh of N squared";
var oN3 = "big Oh of N cubed";
var logN = "big Oh of log N";
var nLogN = "big Oh of N Log of N";
var factN = "big Oh of N factorial";
var exp = "big Oh of 2 to the N";
var c = "constant"
var ePlusV = "big Oh of the total number of edges and vertices";

var facts = [];
facts.push("Array indexing for linear and dynamic is " + c);
facts.push("Array search is " + oN);
facts.push("Array insertion for dynamic is " + oN);
facts.push("Linked list indexing is " + oN);
facts.push("Linked list search is " + oN);
facts.push("Linked list insertion is " + c);
facts.push("Hash table indexing is " + c);
facts.push("Hash table search is " + c);
facts.push("Hash table insertion is " + c);
facts.push("Binary tree indexing is " + logN);
facts.push("Binary tree search is " + logN);
facts.push("Binary tree insertion is " + logN);
facts.push("Breadth First Search runtime is " + ePlusV);
facts.push("Depth First Search run time is " + ePlusV);
facts.push("Merge Sort Best case is " + oN);
facts.push("Merge Sort Average case is " + nLogN);
facts.push("Merge Sort Worse case is " + nLogN);
facts.push("Quick Sort Best case is " + oN);
facts.push("Quick Sort Average case is " + nLogN);
facts.push("Quick Sort Worse case is " + oN2);
facts.push("Bubble Sort Best case is " + oN);
facts.push("Bubble Sort Average case is " + oN2);
facts.push("Bubble Sort Worse case is " + oN2);

exports.bank = facts;
