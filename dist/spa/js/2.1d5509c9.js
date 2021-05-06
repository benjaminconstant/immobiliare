(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[2],{"1de0":function(e,t,l){},"76a5":function(e,t,l){"use strict";l("1de0")},"8b24":function(e,t,l){"use strict";l.r(t);var a=function(){var e=this,t=e.$createElement,l=e._self._c||t;return l("q-page",{staticClass:"flex flex-center"},[l("div",{staticClass:"q-pa-xl"},[l("Table")],1)])},n=[],i=function(){var e=this,t=e.$createElement,l=e._self._c||t;return l("q-table",{ref:"table",staticClass:"bg-grey-5 q-pa-xl",attrs:{dense:"","hide-bottom":"","wrap-cells":"",pagination:e.pagination,"binary-state-sort":"",data:e.houses,columns:e.columns,"row-key":"id",filter:e.filter},scopedSlots:e._u([{key:"top",fn:function(){return[l("div",{staticClass:"row justify-around fit items-center text-secondary"},[l("q-select",{attrs:{filled:"",color:"secondary",label:"Ricerca",options:e.searchOptions},on:{input:function(t){return e.onSearchChange(t)}},model:{value:e.selectedSearch,callback:function(t){e.selectedSearch=t},expression:"selectedSearch"}}),l("q-input",{attrs:{clearable:"",color:"secondary",placeholder:"Cerca"},model:{value:e.filter,callback:function(t){e.filter=t},expression:"filter"}}),l("h4",[e._v("\n        "+e._s(e.houseCounter)+" Annunci\n      ")]),l("span",[e._v("ultimo aggiornamento: "+e._s(e.lastUpdate))]),l("q-toggle",{attrs:{color:"secondary",label:e.isHidden?"Nascoste":"Visibili"},model:{value:e.isHidden,callback:function(t){e.isHidden=t},expression:"isHidden"}})],1),l("div",{staticClass:"row q-pb-lg items-center fit text-secondary q-gutter-md"},[l("div",{staticClass:"col q-gutter-md"},[l("FilterInput",{attrs:{"field-name":"price_min","field-label":"Prezzo MIN"}}),l("FilterInput",{attrs:{"field-name":"price_max","field-label":"Prezzo MAX"}})],1),l("div",{staticClass:"col q-gutter-md"},[l("FilterInput",{attrs:{"field-name":"price_mq_min","field-label":"Prezzo MQ MIN"}}),l("FilterInput",{attrs:{"field-name":"price_mq_max","field-label":"Prezzo MQ MAX"}})],1),l("div",{staticClass:"col q-gutter-md"},[l("FilterInput",{attrs:{"field-name":"mq_min","field-label":"MQ MIN"}}),l("FilterInput",{attrs:{"field-name":"mq_max","field-label":"MQ MAX"}})],1),l("div",{staticClass:"col q-gutter-md"},[l("FilterInput",{attrs:{"field-name":"costs_min","field-label":"Spese MIN"}}),l("FilterInput",{attrs:{"field-name":"costs_max","field-label":"Spese MAX"}})],1),l("div",{staticClass:"col q-gutter-md"},[l("FilterSelect",{attrs:{"field-name":"state","field-label":"Stato"}})],1)])]},proxy:!0},{key:"body-cell-link",fn:function(e){return[l("q-td",[l("q-btn",{staticClass:"text-bold text-white",attrs:{"no-caps":"",type:"a",color:"secondary",target:"_blank",href:e.row.link,label:"Link"}})],1)]}},{key:"body-cell-title",fn:function(t){return[l("q-td",{staticStyle:{"max-width":"400px"}},[e._v("\n      "+e._s(t.row.title)+"\n      "),l("q-tooltip",{attrs:{"content-class":"bg-dark","content-style":"font-size: 20px","max-width":"50vw"}},[e._v("\n        "+e._s(t.row.text)+"\n      ")])],1)]}},{key:"body-cell-is_interesting",fn:function(t){return[l("q-td",[l("q-icon",{attrs:{color:t.row.is_interesting?"warning":"grey",name:"star",size:"lg"},on:{click:function(l){return e.$store.dispatch("putInteresting",t.row)}}})],1)]}},{key:"body-cell-price_mq",fn:function(t){return[l("q-td",[l("span",{class:e.price_mqColor(t.row.price_mq)},[e._v("\n        "+e._s(t.row.price_mq.toFixed(2))+"\n      ")])])]}},{key:"body-cell-costs",fn:function(t){return[l("q-td",[l("span",{class:e.costsColor(t.row.costs)},[e._v("\n        "+e._s(e.formatCurrency(t.row.costs))+"\n      ")])])]}},{key:"body-cell-is_hidden",fn:function(t){return[l("q-td",[l("q-btn",{attrs:{label:e.isHidden?"Ripristina":"Nascondi",color:e.isHidden?"positive":"negative"},on:{click:function(l){return e.$store.dispatch("putHidden",t.row)}}})],1)]}}])})},r=[],s=l("ded3"),o=l.n(s),c=(l("ddb0"),function(){var e=this,t=e.$createElement,l=e._self._c||t;return l("q-input",{attrs:{clearable:"",filled:"",color:"secondary",label:e.fieldLabel,value:e.filters[e.fieldName],debounce:"500"},on:{input:function(t){return e.onFilterChange(t)}}})}),d=[],u=l("2f62"),f={name:"FilterInput",props:{fieldName:{type:String,default:String},fieldLabel:{type:String,default:String}},data(){return{}},computed:o()({},Object(u["d"])(["filters"])),methods:o()(o()({},Object(u["c"])(["updateFilter"])),{},{onFilterChange(e){this.updateFilter({key:this.fieldName,value:e}),this.$store.dispatch("getHouses")}})},p=f,m=l("2877"),b=l("27f9"),h=l("eebe"),g=l.n(h),y=Object(m["a"])(p,c,d,!1,null,null,null),v=y.exports;g()(y,"components",{QInput:b["a"]});var _=function(){var e=this,t=e.$createElement,l=e._self._c||t;return l("q-select",{attrs:{filled:"",color:"secondary",label:e.fieldLabel,options:e.options,debounce:"500"},on:{input:function(t){return e.onFilterChange(t)}},model:{value:e.value,callback:function(t){e.value=t},expression:"value"}})},x=[],q={name:"FilterInput",props:{fieldName:{type:String,default:String},fieldLabel:{type:String,default:String}},data(){return{value:{label:"Tutti",value:0},options:[{label:"Tutti",value:0},{label:"Da Ristrutturare",value:1},{label:"Buono / Abitabile",value:2},{label:"Ottimo / Ristrutturato",value:3},{label:"Nuovo / In costruzione",value:4},{label:"N.D.",value:5}]}},computed:o()({},Object(u["d"])(["filters"])),methods:o()(o()({},Object(u["c"])(["updateFilter"])),{},{onFilterChange(e){this.updateFilter({key:this.fieldName,value:e.value}),this.$store.dispatch("getHouses")}})},w=q,C=l("ddd8"),S=Object(m["a"])(w,_,x,!1,null,null,null),k=S.exports;g()(S,"components",{QSelect:C["a"]});var F=l("bd4c"),I={name:"Table",components:{FilterInput:v,FilterSelect:k},data(){return{selectedSearch:"",isHidden:!1,filter:"",pagination:{sortBy:"created",descending:!0,rowsPerPage:0},columns:[{name:"date_publish",label:"Pubblicato",align:"left",field:e=>e.date_publish,format:e=>F["a"].formatDate(e,"DD-MM-YYYY"),sortable:!0},{name:"created",label:"Creato",align:"left",field:e=>e.created,format:e=>F["a"].formatDate(e,"DD-MM-YYYY"),sortable:!0},{name:"title",label:"Titolo",align:"left",field:e=>e.title,sortable:!0},{name:"costs",label:"Spese",align:"left",field:e=>e.costs,format:e=>this.formatCurrency(e),sortable:!0},{name:"mq",label:"MQ",align:"left",field:e=>e.mq,sortable:!0},{name:"price_mq",label:"Prezzo MQ",align:"left",field:e=>e.price_mq,format:e=>this.formatCurrency(e),sortable:!0},{name:"price",label:"Prezzo",align:"left",field:e=>e.price,format:e=>this.formatCurrency(e),sortable:!0},{name:"link",label:"Link",align:"left",field:e=>e.link},{name:"text",headerStyle:"display: none",style:"display: none",label:"Descrizione",align:"left",field:e=>e.text},{name:"is_hidden",label:"",align:"left",field:e=>e.is_interesting},{name:"is_interesting",label:"",align:"left",field:e=>e.is_interesting}]}},computed:o()(o()({},Object(u["b"])(["housesHidden, housesVisible"])),{},{searchOptions(){return this.$store.state.searches.map((e=>({label:e.name,value:e.id})))},houses(){return this.isHidden?this.$store.getters.housesHidden:this.$store.getters.housesVisible},lastUpdate(){return F["a"].formatDate(new Date(Math.max(...this.houses.map((e=>new Date(e.updated))))),"DD/MM/YYYY - HH:mm")},houseCounter(){return this.filter?this.$refs.table.filteredSortedRowsNumber:this.houses.length}}),mounted(){this.$store.dispatch("getSearches").then((()=>{this.selectedSearch=this.searchOptions[0],this.$store.dispatch("getHouses")})),setInterval((()=>this.$store.dispatch("getHouses")),1e4)},methods:o()(o()({},Object(u["c"])(["updateFilter"])),{},{onSearchChange(e){this.updateFilter({key:"searches",value:e.value}),this.$store.dispatch("getHouses")},formatCurrency(e){return null!==e?e.toLocaleString("it-IT",{style:"currency",currency:"EUR"}):"N.D."},price_mqColor(e){return e<500?"text-green-10":e<1e3?"text-green-5":e<1250?"text-yellow":e<1500?"text-red":e>=1500?"text-deep-purple-14":void 0},costsColor(e){return e<0?"text-black":e<25?"text-green-10":e<50?"text-green-5":e<75?"text-yellow":e<100?"text-red":e>=100?"text-deep-purple-14":void 0}})},M=I,H=(l("76a5"),l("eaac")),Q=l("9564"),z=l("db86"),$=l("9c40"),D=l("05c0"),N=l("0016"),O=Object(m["a"])(M,i,r,!1,null,null,null),Y=O.exports;g()(O,"components",{QTable:H["a"],QSelect:C["a"],QInput:b["a"],QToggle:Q["a"],QTd:z["a"],QBtn:$["a"],QTooltip:D["a"],QIcon:N["a"]});var j={name:"Index",components:{Table:Y}},T=j,P=l("9989"),L=Object(m["a"])(T,a,n,!1,null,null,null);t["default"]=L.exports;g()(L,"components",{QPage:P["a"]})}}]);