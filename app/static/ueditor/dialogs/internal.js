(function () {
    var parent = window.parent;
    //dialogÂØπË±°
    dialog = parent.$EDITORUI[window.frameElement.id.replace( /_iframe$/, '' )];
    //ÂΩìÂâçÊâìÂºÄdialogÁöÑÁºñËæëÂô®ÂÆû‰æã
    editor = dialog.editor;

    UE = parent.UE;

    domUtils = UE.dom.domUtils;

    utils = UE.utils;

    browser = UE.browser;

    ajax = UE.ajax;

    $G = function ( id ) {
        return document.getElementById( id )
    };
    //focusÂÖÉÁ¥†
    $focus = function ( node ) {
        setTimeout( function () {
            if ( browser.ie ) {
                var r = node.createTextRange();
                r.collapse( false );
                r.select();
            } else {
                node.focus()
            }
        }, 0 )
    };
    utils.loadFile(document,{
        href:editor.options.themePath + editor.options.theme + "/dialogbase.css?cache="+Math.random(),
        tag:"link",
        type:"text/css",
        rel:"stylesheet"
    });
    lang = editor.getLang(dialog.className.split( "-" )[2]);
    if(lang){
        domUtils.on(window,'load',function () {

            var langImgPath = editor.options.langPath + editor.options.lang + "/images/";
            //ÈíI.opl"}}ôbÄÅËµÑÊ∫ê           //f = (ar lai inangIm[tylatic"] {
                var r mUt ed$Gid ;
                r.(la!mUt) continue                r.r r g:"me.s dia.dog:"me.s,               r.....contt = wingIm[tylatic"][i]                r.(lacontt =.src)                va  //Èíclone               r.....contt = wiils.lot/cend({},contt =,lse )
                r.....contt =.src wingImgPath = +.contt =.src                r.}               r.(lacontt =.slesh)                va  //contt = wiils.lot/cend({},contt =,lse )
                r.....contt =.slesh wicontt =.slesheplace( //url\s*\(/g,"url(" +.ngImgPath =)               r.}               r.switch (ag:"me.s.toLowerCe.c {
{
                va....ce.c "r r":               va........a.dorent.UNe.foplace( Chil idcument.geeateTextRaNe.f(/contt = )u mUt sh)                va      b/c              r.r r g:"me.s dia.dHext"U;[rtk"",i      r.r r Oö$ngI[}er g0, oj; ojr g.r [j];  r.}               r.swiiiiiiiiioj.innerHTML{},contt =,.s dia.[j++me.s,                       //url\s*\(/g,"url    r.r r Oö$ngI[}p    dorent.UNr.}               r.swiiiiiiiiip != ".s dia." &&g:"meusÂAttribut.a.p, dorent.[p]lace( Chil idcument.geeateTe //url\s*\(/g,"url    r.r xtRaNe.f(/contt = )u mUt shdefault e.s.toLowerCe.c {
{
         ssNameusÂAttribut.s    m, dorent.ace( Chil idcument. //url\s*\(/g,} else {
  lace( Ch}


})    
