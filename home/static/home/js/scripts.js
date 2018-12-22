var buttonLeft = document.getElementsByClassName('button-left')[0];
 var buttonRight = document.getElementsByClassName('button-right')[0];
 var slide = document.getElementsByClassName('slides');
 j = 1;
 r = 2;
 l = 0;
 k = 1;
 original = true;
 buttonLeft.addEventListener('click', function (event) {
 	if( j < 0){
 		j = j + 2;
 	}
 	if( k > 2){
 		k = k-2;
 	}

 	console.log('before left transition ' + j );
 	if( l == 0){

 		for (var i = 0; i <slide.length; i++) {
     	pos = -200
     	pos = pos + '%';
     	slide[i].style.transform = 'translateX('+pos+')';
     }
     l = 2;
     j = 1;
     r = 0;
     k = 1;
 	}
 	else {

	    for (var i = 0; i <slide.length; i++) {
	    	pos = -100 * j;
	     	pos = pos + '%';
	     	slide[i].style.transform = 'translateX('+pos+')';
	     }
	     console.log(pos)
	     j--;
	     l--;
	     r++;
	     k++;
	     console.log(j)
	}
 });

 buttonRight.addEventListener('click', function (event) {
    if( j < 0){
 		j = j + 2;
 	}
 	if( k > 2){
 		k = k-2;
 	}
 	console.log('before left transition ' + j );
 	if( r == 0){

 		for (var i = 0; i <slide.length; i++) {
     	pos = 0;
     	pos = pos + '%';
     	slide[i].style.transform = 'translateX('+pos+')';
     }
     r = 2;
     k = 1;
     l = 0;
     j = 1;
 	}
 	else {

	    for (var i = 0; i <slide.length; i++) {
	     	pos = -100*k
	     	pos = pos + '%';
	     	slide[i].style.transform = 'translateX('+pos+')';
	     }
	     console.log(pos)
	     k++;
	     l++;
	     r--;
	     j--;
	     console.log(j)
	}

 });