!function(e,t){"function"==typeof define&&define.amd?require(["jquery"],t):e.amdWeb=t(e.jQuery)}("undefined"!=typeof self?self:this,function(e){e(document).ready(function(){function t(t){if(!t.id)return t.text;var n=t.element instanceof Array?t.element[0].value:t.element.value;return e("<span class='fa-icon fa-"+n+"'></span><span>"+t.text+"</span>")}var n=function(){e(".datagridwidget-body tr:not(.datagridwidget-empty-row) select.select-widget").select2({width:"100%",templateResult:t,templateSelection:t,formatResult:t,formatSelection:t}),e(".z3cformInlineValidation").removeClass("z3cformInlineValidation")};if(1===e("#service-edit-form").length)if(e.fn.select2)n();else{var i=portal_url+"/++resource++servicenavigation/select2-4.0.0/dist",r=i+"/js/select2.min.js";e.getScript(r,function(){e("head").append(e('<link rel="stylesheet" type="text/css" />').attr("href",i+"/css/select2.min.css")),n()})}e(".select-widget, .datagridwidget-row").change(function(){n()}),e(".insert-row").click(function(){n()})})}),define("service-edit-form",function(){}),require(["service-edit-form"],function(e){}),define("main",function(){});