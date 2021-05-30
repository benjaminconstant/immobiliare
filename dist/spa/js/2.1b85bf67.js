(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[2],{"1de0":function(e,t,a){},"76a5":function(e,t,a){"use strict";a("1de0")},"8b24":function(e,t,a){"use strict";a.r(t);var l=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("q-page",{staticClass:"flex flex-center"},[a("div",{staticClass:"q-pa-xl"},[a("Table")],1)])},n=[],r=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("q-table",{ref:"table",staticClass:"bg-grey-5 q-pa-xl",attrs:{dense:"","hide-bottom":"","wrap-cells":"",pagination:e.pagination,loading:e.pending,separator:"cell","binary-state-sort":"",data:e.houses,color:"secondary",columns:e.columns,"row-key":"id",filter:e.filter},scopedSlots:e._u([{key:"top",fn:function(){return[a("div",{staticClass:"row justify-around fit items-center text-secondary"},[a("q-select",{attrs:{filled:"",color:"secondary",label:"Ricerca",options:e.searchOptions},on:{input:function(t){return e.onSearchChange(t)}},model:{value:e.selectedSearch,callback:function(t){e.selectedSearch=t},expression:"selectedSearch"}}),a("q-input",{attrs:{clearable:"",debounce:"500",color:"secondary",placeholder:"Cerca"},model:{value:e.filter,callback:function(t){e.filter=t},expression:"filter"}}),a("h4",[e._v("\n        "+e._s(e.houseCounter)+" Annunci\n      ")]),a("q-btn",{attrs:{unelevated:"",outline:"",icon:"refresh"},on:{click:function(t){return e.$store.dispatch("getHouses")}}}),a("span",[e._v("ultimo aggiornamento: "+e._s(e.lastUpdate))]),a("q-toggle",{attrs:{color:"secondary",label:e.isHidden?"Nascoste":"Visibili"},model:{value:e.isHidden,callback:function(t){e.isHidden=t},expression:"isHidden"}})],1),a("div",{staticClass:"row q-pb-lg items-center fit text-secondary q-gutter-md"},[a("div",{staticClass:"col q-gutter-md"},[a("FilterInput",{attrs:{"field-name":"price_min","field-label":"Prezzo MIN"}}),a("FilterInput",{attrs:{"field-name":"price_max","field-label":"Prezzo MAX"}})],1),a("div",{staticClass:"col q-gutter-md"},[a("FilterInput",{attrs:{"field-name":"price_mq_min","field-label":"Prezzo MQ MIN"}}),a("FilterInput",{attrs:{"field-name":"price_mq_max","field-label":"Prezzo MQ MAX"}})],1),a("div",{staticClass:"col q-gutter-md"},[a("FilterInput",{attrs:{"field-name":"mq_min","field-label":"MQ MIN"}}),a("FilterInput",{attrs:{"field-name":"mq_max","field-label":"MQ MAX"}})],1),2!=e.selectedSearch.platform?a("div",{staticClass:"col q-gutter-md"},[a("FilterInput",{attrs:{"field-name":"costs_min","field-label":"Spese MIN"}}),a("FilterInput",{attrs:{"field-name":"costs_max","field-label":"Spese MAX"}})],1):e._e(),2!=e.selectedSearch.platform?a("div",{staticClass:"col q-gutter-md"},[a("FilterSelect",{attrs:{"field-name":"state","field-label":"Stato"}})],1):e._e()])]},proxy:!0},{key:"body-cell-link",fn:function(e){return[a("q-td",{staticClass:"text-center"},[a("q-btn",{staticClass:"text-bold text-white",attrs:{"no-caps":"",type:"a",color:"secondary",target:"_blank",href:e.row.link,label:"Link"}})],1)]}},{key:"body-cell-created",fn:function(t){return[a("q-td",{staticClass:"text-center"},[a("span",{class:e.date.isSameDate(t.row.created,new Date,"day")?"text-warning":""},[e._v(e._s(e.date.formatDate(t.row.created,"DD-MM-YYYY")))])])]}},{key:"body-cell-title",fn:function(t){return[a("q-td",{staticClass:"text-center",class:{"bg-red":!t.row.has_changed},staticStyle:{"max-width":"400px"}},[e._v("\n      "+e._s(t.row.title)+"\n      "),a("q-tooltip",{attrs:{"content-class":"bg-dark","content-style":"font-size: 20px","max-width":"50vw"}},[e._v("\n        "+e._s(t.row.text)+"\n      ")]),t.row.has_changed?e._e():a("q-icon",{attrs:{size:"lg",color:"negative",name:"delete"},on:{click:function(a){return e.$store.dispatch("deleteHouse",t.row)}}})],1)]}},{key:"body-cell-is_interesting",fn:function(t){return[a("q-td",{staticClass:"text-center"},[a("div",[a("q-icon",{attrs:{size:"lg",color:t.row.is_interesting?"warning":"grey",name:"star"},on:{click:function(a){return e.$store.dispatch("putInteresting",t.row)}}}),a("q-icon",{attrs:{size:"lg",color:t.row.is_hidden?"positive":"negative",name:t.row.is_hidden?"restore":"delete"},on:{click:function(a){return e.$store.dispatch("putHidden",t.row)}}})],1)])]}},{key:"body-cell-price_mq",fn:function(t){return[a("q-td",{staticClass:"text-center"},[a("span",{class:e.price_mqColor(t.row.price_mq)},[e._v("\n        "+e._s(e._f("currency")(t.row.price_mq))+"\n      ")])])]}},{key:"body-cell-costs",fn:function(t){return[a("q-td",{staticClass:"text-center"},[a("span",{class:e.costsColor(t.row.costs)},[e._v("\n        "+e._s(e.formatCurrency(t.row.costs))+"\n      ")])])]}},{key:"body-cell-is_private",fn:function(t){return[a("q-td",{staticClass:"text-center",class:t.row.is_private&&"bg-positive"},[a("div",{staticClass:"row",staticStyle:{width:"20vw"}},e._l(t.row.image_set,(function(e){return a("q-intersection",{key:e.url,staticClass:"col q-mx-xs",attrs:{once:"",transition:"scale"}},[a("q-img",{attrs:{src:e.url}},[a("q-tooltip",[a("q-img",{staticStyle:{width:"30vw"},attrs:{src:e.url}})],1)],1)],1)})),1)])]}},{key:"body-cell-note",fn:function(t){return[a("q-td",{staticClass:"text-center"},[a("q-input",{attrs:{autogrow:"",value:t.row.note,type:"textarea",debounce:"500"},on:{input:function(a){return e.onNoteChange(t.row,a)}}})],1)]}}])})},s=[],i=a("ded3"),o=a.n(i),c=(a("ddb0"),function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("q-input",{attrs:{clearable:"",filled:"",color:"secondary",label:e.fieldLabel,value:e.filters[e.fieldName],debounce:"500"},on:{input:function(t){return e.onFilterChange(t)}}})}),d=[],u=a("2f62"),p={name:"FilterInput",props:{fieldName:{type:String,default:String},fieldLabel:{type:String,default:String}},data(){return{}},computed:o()({},Object(u["d"])(["filters"])),methods:o()(o()({},Object(u["c"])(["updateFilter"])),{},{onFilterChange(e){this.updateFilter({key:this.fieldName,value:e}),this.$store.dispatch("getHouses")}})},f=p,m=a("2877"),b=a("27f9"),h=a("eebe"),g=a.n(h),y=Object(m["a"])(f,c,d,!1,null,null,null),v=y.exports;g()(y,"components",{QInput:b["a"]});var _=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("q-select",{attrs:{filled:"",color:"secondary",label:e.fieldLabel,options:e.options,debounce:"500"},on:{input:function(t){return e.onFilterChange(t)}},model:{value:e.value,callback:function(t){e.value=t},expression:"value"}})},x=[],w={name:"FilterInput",props:{fieldName:{type:String,default:String},fieldLabel:{type:String,default:String}},data(){return{value:{label:"Tutti",value:0},options:[{label:"Tutti",value:0},{label:"Da Ristrutturare",value:1},{label:"Buono / Abitabile",value:2},{label:"Ottimo / Ristrutturato",value:3},{label:"Nuovo / In costruzione",value:4},{label:"N.D.",value:5}]}},computed:o()({},Object(u["d"])(["filters"])),methods:o()(o()({},Object(u["c"])(["updateFilter"])),{},{onFilterChange(e){this.updateFilter({key:this.fieldName,value:e.value}),this.$store.dispatch("getHouses")}})},q=w,C=a("ddd8"),k=Object(m["a"])(q,_,x,!1,null,null,null),S=k.exports;g()(k,"components",{QSelect:C["a"]});var F=a("bd4c"),I={name:"Table",components:{FilterInput:v,FilterSelect:S},data(){return{date:F["a"],selectedSearch:"",isHidden:!1,filter:"",pagination:{sortBy:"created",descending:!0,rowsPerPage:0},columns:[{name:"date_publish",label:"Data",align:"left",field:e=>e.date_publish,format:e=>F["a"].formatDate(e,"DD-MM-YYYY"),sortable:!0,style:"min-width: 110px"},{name:"created",label:"Creato",align:"left",field:e=>e.created,format:e=>F["a"].formatDate(e,"DD-MM-YYYY"),sortable:!0,style:"min-width: 110px"},{name:"title",label:"Titolo",align:"left",field:e=>e.has_changed,sortable:!0},{name:"is_private",label:"Galleria",align:"left",field:e=>e.is_private,sortable:!0},{name:"costs",label:"Spese",align:"left",field:e=>e.costs,format:e=>this.formatCurrency(e),sortable:!0},{name:"mq",label:"MQ",align:"left",field:e=>e.mq,sortable:!0},{name:"price_mq",label:"Prezzo MQ",align:"left",field:e=>e.price_mq,format:e=>this.formatCurrency(e),sortable:!0},{name:"price",label:"Prezzo",align:"left",field:e=>e.price,format:e=>this.formatCurrency(e),sortable:!0},{name:"link",label:"Link",align:"left",field:e=>e.link},{name:"text",headerStyle:"display: none",style:"display: none",label:"Descrizione",align:"left",field:e=>e.text},{name:"is_interesting",label:"",align:"left",field:e=>e.is_interesting,sortable:!0},{name:"note",label:"Note",align:"left",field:e=>e.note}]}},computed:o()(o()(o()({},Object(u["b"])(["housesHidden, housesVisible"])),Object(u["d"])(["pending"])),{},{searchOptions(){return this.$store.state.searches.map((e=>({label:e.name,value:e.id,platform:e.platform})))},houses(){return this.isHidden?this.$store.getters.housesHidden:this.$store.getters.housesVisible},lastUpdate(){return F["a"].formatDate(new Date(Math.max(...this.houses.map((e=>new Date(e.updated))))),"DD/MM/YYYY - HH:mm")},houseCounter(){return this.filter?this.$refs.table.filteredSortedRowsNumber:this.houses.length}}),watch:{selectedSearch:function(e){2===e&&(this.updateFilter({key:"state",value:null}),this.updateFilter({key:"costs_min",value:null}),this.updateFilter({key:"costs_max",value:null}))}},mounted(){this.$store.dispatch("getSearches").then((()=>{this.selectedSearch=this.searchOptions[0],this.updateFilter({key:"search",value:this.selectedSearch.value}),this.$store.dispatch("getHouses")}))},methods:o()(o()({},Object(u["c"])(["updateFilter"])),{},{onSearchChange(e){this.updateFilter({key:"search",value:e.value}),this.$store.dispatch("getHouses")},onNoteChange(e,t){e.note=t,this.$store.dispatch("putNote",e)},formatCurrency(e){return null!==e?e.toLocaleString("it-IT",{style:"currency",currency:"EUR"}):"N.D."},price_mqColor(e){return e<500?"text-green-10":e<1e3?"text-green-5":e<1250?"text-yellow":e<1500?"text-red":e>=1500?"text-deep-purple-14":void 0},costsColor(e){return e<0?"text-black":e<25?"text-green-10":e<50?"text-green-5":e<75?"text-yellow":e<100?"text-red":e>=100?"text-deep-purple-14":void 0}})},M=I,D=(a("76a5"),a("eaac")),Q=a("9c40"),z=a("9564"),N=a("db86"),$=a("05c0"),H=a("0016"),Y=a("ad56"),O=a("068f"),j=Object(m["a"])(M,r,s,!1,null,null,null),T=j.exports;g()(j,"components",{QTable:D["a"],QSelect:C["a"],QInput:b["a"],QBtn:Q["a"],QToggle:z["a"],QTd:N["a"],QTooltip:$["a"],QIcon:H["a"],QIntersection:Y["a"],QImg:O["a"]});var P={name:"Index",components:{Table:T}},L=P,A=a("9989"),E=Object(m["a"])(L,l,n,!1,null,null,null);t["default"]=E.exports;g()(E,"components",{QPage:A["a"]})}}]);