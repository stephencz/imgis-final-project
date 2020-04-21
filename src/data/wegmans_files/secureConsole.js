"use strict";

//  Stop all console.log() outputs:
function clearConsoleMethods() {
    var console = (window.console = window.console || {});
    console["log"] = function (){ 
        // NOP (Note: IE doesn't like arrow functin expressions. 0905.)
    };
}
clearConsoleMethods();
