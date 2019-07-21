// File: myFunctions.js
// Author: Haomin He
//
//////////////////////////////////////////////////////////////////////
function sum_of_mults_below_n(N) {
	var i = 1, ans = '', sum = 0;

	while (i < N) {
		//(N > 0)
		//test: multiple of 3 or 5?

		if ((i % 3 == 0) || (i % 5 == 0)) {
			sum += i;
			ans = ans + i + ' ';
		}++i;
	}
	return sum;
}

function sumOfMults1000() {
	var i = 1, ans = '', sum = 0;

	//generate natural numbers 1 .. 999
	while (i < 1000) {
		//test: multiple of 3 or 5?
		if ((i % 3 == 0) || (i % 5 == 0)) {
			sum += i;
			ans = ans + i + ' ';
		}++i;
	}
	return sum;
}

function reverse(s) {
	return s.split('').reverse().join('');
}

function isPal(s) {
	var s = s.toUpperCase();

	if (s == reverse(s))
		return true;
	else
		return false;
}

function zapPunct(phrase) {
	var index, phrase;
	index = phrase.search(/[ .,;:'!\?#]/);
	while (index != -1) {
		phrase = phrase.substring(0, index) + phrase.substring(index + 1, phrase.length);
		index = phrase.search(/[ .,;:'!\?#]/);
	}
	return phrase;
}