(function(f) {
  var haveAUI = typeof P !== 'undefined' && P.AUI_BUILD_DATE;
  if (typeof SiegeCrypto !== 'undefined') {
    var ret = f(SiegeCrypto);
    if (haveAUI) {
      P.declare('siege-cse:profile:Wfm-DigitalTech-StoreFinder-Query', ret);
    }
  } else if (haveAUI) {
    P.when('siege-cse').register('siege-cse:profile:Wfm-DigitalTech-StoreFinder-Query', f);
  } else {
    throw new Error("CSE library not loaded");
  }
})(function(SiegeCrypto) {

SiegeCrypto.addProfile("Wfm-DigitalTech-StoreFinder-Query", {
  "query": {dataType: "Wfm-DigitalTech-StoreFinder-Query"},
});

var createDeferred = SiegeCrypto.createDeferred || (function() {
  return {
    resolve: function() {},
    reject: function(e) {
      console.error(e);
    }
  };
});

function downloadDataType(id) {
  var deferred = createDeferred();

  try {
    var cseScriptNode = document.createElement('script');
    cseScriptNode.onload = deferred.resolve;
    cseScriptNode.onerror = deferred.reject.bind(null,
      new Error('Script failed to load for datatype "' + id + '"'));
    cseScriptNode.src = 'https://static.siege-amazon.com/prod/keys/' + id + '.js';
    document.head.appendChild(cseScriptNode);
  } catch (e) {
    deferred.reject(e);
  }

  if (SiegeCrypto.addLoadingDataType) {
    SiegeCrypto.addLoadingDataType(id, deferred.promise);
  }
}

downloadDataType("Wfm-DigitalTech-StoreFinder-Query");

return SiegeCrypto;

});
