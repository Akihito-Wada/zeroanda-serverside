var LoggerLevel={
  ALL:-99,
  DEBUG:-1,
  INFO:0,
  WARN:1,
  ERROR:2,
  OFF:99
};
var Logger=function(level){
  var self=this;
  self.level=isNaN(level) ? LoggerLevel.INFO : level;
  self.make();
};
Logger.prototype.make=function(){
  var self=this;
  for(var key in console){
    var l=LoggerLevel[key.toUpperCase()];
    if(!l){l=LoggerLevel.OFF};
    if(self.level<=l){
      if(Function.bind){
        Logger.prototype[key]=(
          function(k){
            return console[k].bind(console);
          }
        )(key);
      }else{
        Logger.prototype[key]=(
          function(k){
            return console[k].apply(console, arguments);
          }
        )(key);
      }
    }else{
      Logger.prototype[key]=function(){};
    }
  }
};

var logger = new Logger(LoggerLevel.ALL);
