function getActiveSheet() {
  var app = SpreadsheetApp;
  var ss = app.getActiveSpreadsheet();
  var activeSheet = ss.getActiveSheet();
  
  activeSheet.getRange(1,2,50).setValue('');
  
  for(i=1; i<=50; i++) {
    if(activeSheet.getRange("A" + i).getValue() != '') {
      activeSheet.getRange("B" + i).setValue("Done printing!");
    }
  }
}


function testConfiguration() {
  var app = SpreadsheetApp;
  var ss = app.getActiveSpreadsheet();
  var activeSheet = ss.getActiveSheet();
  var cpService = getCloudPrintService();
  
  if(!cpService.hasAccess()) {
    activeSheet.getRange("C1").setValue(cpService.getAuthorizationUrl());
  } else {
    activeSheet.getRange("C1").setValue("Successfully configured!");
  }
}


function printDocumentsFromSheet() {
  var app = SpreadsheetApp;
  var ss = app.getActiveSpreadsheet();
  var activeSheet = ss.getActiveSheet();
  var printerID = '9b80228c-2c40-10b9-032f-f09a6a3e0ee4';
  
  activeSheet.getRange(1,2,50).setValue('');
  
  for(i=1; i<=50; i++){
    if(activeSheet.getRange("A" + i).getValue() != ''){
      var str = activeSheet.getRange("A" + i).getValue();
      var res = str.split("/");
      var docID = res[5];
      var docName = 'Printing:' + docID;
      var processPrint = printGoogleDocument(docID, printerID, docName);
      activeSheet.getRange("B" + i).setValue(processPrint);
    }
  }
}


function logger() {
  var files = DriveApp.getFiles();
  while (files.hasNext()) {
    var file = files.next();
    Logger.log(file.getName());
  }
  return HtmlService.createHtmlOutput(files);
}


function getCloudPrintService() {
  var authUrl = 'https://accounts.google.com/o/oauth2/auth';
  var tokenUrl = 'https://accounts.google.com/o/oauth2/token';
  var clientID = '167457568247-9tfuniufcbapke0ji7a3e94ljgfifgad.apps.googleusercontent.com';
  var clientSecret = 'HitCiMstTa5h8JddHDAk9mt9';
  var scopeUrl = 'https://www.googleapis.com/auth/cloudprint';
  
  return OAuth2.createService('print')
  .setAuthorizationBaseUrl(authUrl)
  .setTokenUrl(tokenUrl)
  .setClientId(clientID)
  .setClientSecret(clientSecret)
  .setCallbackFunction('authCallback')
  .setPropertyStore(PropertiesService.getUserProperties())
  .setScope(scopeUrl)
  .setParam('login_hint', Session.getActiveUser().getEmail())
  .setParam('access_type', 'offline')
  .setParam('approval_prompt', 'force');
}


function authCallback(request){
  var isAuthorized = getCloudPrintService().handleCallback(request);
  
  if(isAuthorized){
    return HtmlService.createHtmlOutput('You can now use Google Cloud Print from App Script');
  } else {
    return HtmlService.createHtmlOutput('Cloud Print Error: Access Denied');
  }
}


function getPrinterList() {
  var response = UrlFetchApp.fetch('https://www.google.com/cloudprint/search',{
    headers: {
      Authorization: 'Bearer' + getCloudPrintService().getAccessToken()
    },
    muteHttpExceptions: true
  }).getContentText();
  
  var printers = JSON.parse(response).printers;
  
  for(var p in printers){
    Logger.log("%s %s %s", printers[p].id, printers[p].name. printers[p].description);
  }
}


function printGoogleDocument(docID, printerID, docName){
  var ticket = {
    version: "1.0",
    print: {
      color: {
        type: "STANDARD_COLOR",
        vendor_id: "Color"
      },
      duplex: {
        type: "NO_DUPLEX"
      }
    }
  };
  
  var payload = {
    "printerid": printerID,
    "title": docName,
    "content": DriverApp.getFileById(docID).getBlob(),
    "contentType": "application/octet-stream",
    "ticket": JSON.stringify(ticket)
  };
  
  var response = UrlFetchApp.fetch('https://www.google.com/cloudprint/submit', {
    method: 'POST',
    payload: payload,
    headers: {
      Authorization: 'Bearer' + getCloudPrintService().getAccessToken()
    },
    muteHttpExceptions: true
  });
  
  response = JSON.parse(response);
  
  if(response.success) {
    return "%s", response.message;
  } else {
    return "Error Code: %s %s", response.errorCode, response.message;
  }
}
