'use strict';

document.onreadystatechange = function () {
    if(document.readyState === 'complete') {
        document.body.setAttribute("class", "loaded");
    }
};