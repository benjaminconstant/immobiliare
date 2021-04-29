(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[2],{"1de0":function(e,t,l){},"76a5":function(e,t,l){"use strict";l("1de0")},"8b24":function(e,t,l){"use strict";l.r(t);var a=function(){var e=this,t=e.$createElement,l=e._self._c||t;return l("q-page",{staticClass:"flex flex-center"},[l("div",{staticClass:"q-pa-xl"},[l("Table")],1)])},n=[],i=function(){var e=this,t=e.$createElement,l=e._self._c||t;return l("q-table",{staticClass:"bg-grey-5 q-pa-xl",attrs:{dense:"","hide-bottom":"","wrap-cells":"",pagination:e.pagination,"binary-state-sort":"",data:e.houses,columns:e.columns,"row-key":"id",filter:e.filter},scopedSlots:e._u([{key:"top",fn:function(){return[l("div",{staticClass:"row justify-around fit items-center text-secondary"},[l("q-input",{attrs:{clearable:"",color:"secondary",placeholder:"Cerca"},model:{value:e.filter,callback:function(t){e.filter=t},expression:"filter"}}),l("h4",[e._v("\n        "+e._s(e.houses.length)+" Annunci\n      ")]),l("span",[e._v("ultimo aggiornamento: "+e._s(e.lastUpdate))])],1),l("div",{staticClass:"row q-pb-lg items-center fit text-secondary q-gutter-md"},[l("div",{staticClass:"col q-gutter-md"},[l("FilterInput",{attrs:{"field-name":"price_min","field-label":"Prezzo MIN"}}),l("FilterInput",{attrs:{"field-name":"price_max","field-label":"Prezzo MAX"}})],1),l("div",{staticClass:"col q-gutter-md"},[l("FilterInput",{attrs:{"field-name":"price_mq_min","field-label":"Prezzo MQ MIN"}}),l("FilterInput",{attrs:{"field-name":"price_mq_max","field-label":"Prezzo MQ MAX"}})],1),l("div",{staticClass:"col q-gutter-md"},[l("FilterInput",{attrs:{"field-name":"mq_min","field-label":"MQ MIN"}}),l("FilterInput",{attrs:{"field-name":"mq_max","field-label":"MQ MAX"}})],1),l("div",{staticClass:"col q-gutter-md"},[l("FilterInput",{attrs:{"field-name":"costs_min","field-label":"Spese MIN"}}),l("FilterInput",{attrs:{"field-name":"costs_max","field-label":"Spese MAX"}})],1)])]},proxy:!0},{key:"body-cell-link",fn:function(e){return[l("q-td",[l("q-btn",{staticClass:"text-bold text-white",attrs:{"no-caps":"",type:"a",color:"secondary",target:"_blank",href:e.row.link,label:"Link"}})],1)]}},{key:"body-cell-title",fn:function(t){return[l("q-td",{staticStyle:{"max-width":"400px"}},[e._v("\n      "+e._s(t.row.title)+"\n      "),l("q-tooltip",{attrs:{"content-class":"bg-dark","content-style":"font-size: 20px","max-width":"50vw"}},[e._v("\n        "+e._s(t.row.text)+"\n      ")])],1)]}},{key:"body-cell-is_interesting",fn:function(t){return[l("q-td",[l("q-icon",{attrs:{color:t.row.is_interesting?"warning":"grey",name:"star",size:"lg"},on:{click:function(l){return e.$store.dispatch("putInteresting",t.row)}}})],1)]}},{key:"body-cell-price_mq",fn:function(t){return[l("q-td",[l("span",{class:e.price_mqColor(t.row.price_mq)},[e._v("\n        "+e._s(t.row.price_mq.toFixed(2))+"\n      ")])])]}}])})},r=[],s=l("ded3"),o=l.n(s),c=(l("ddb0"),function(){var e=this,t=e.$createElement,l=e._self._c||t;return l("q-input",{attrs:{clearable:"",filled:"",color:"secondary",label:e.fieldLabel,value:e.filters[e.fieldName],debounce:"500"},on:{input:function(t){return e.onFilterChange(t)}}})}),d=[],u=l("2f62"),f={name:"FilterInput",props:{fieldName:{type:String,default:String},fieldLabel:{type:String,default:String}},data(){return{}},computed:o()({},Object(u["c"])(["filters"])),methods:o()(o()({},Object(u["b"])(["updateFilter"])),{},{onFilterChange(e){this.updateFilter({key:this.fieldName,value:e}),this.$store.dispatch("getHouses")}})},p=f,m=l("2877"),b=l("27f9"),g=l("eebe"),_=l.n(g),y=Object(m["a"])(p,c,d,!1,null,null,null),h=y.exports;_()(y,"components",{QInput:b["a"]});var q=l("bd4c"),x={name:"Table",components:{FilterInput:h},data(){return{filter:"",pagination:{sortBy:"date_publish",descending:!0,rowsPerPage:0},columns:[{name:"date_publish",label:"Pubblicato",align:"left",field:e=>e.date_publish,sortable:!0},{name:"title",label:"Titolo",align:"left",field:e=>e.title,sortable:!0},{name:"costs",label:"Spese",align:"left",field:e=>e.costs,format:e=>this.formatCurrency(e),sortable:!0},{name:"mq",label:"MQ",align:"left",field:e=>e.mq,sortable:!0},{name:"price_mq",label:"Prezzo MQ",align:"left",field:e=>e.price_mq,format:e=>this.formatCurrency(e),sortable:!0},{name:"price",label:"Prezzo",align:"left",field:e=>e.price,format:e=>this.formatCurrency(e),sortable:!0},{name:"link",label:"Link",align:"left",field:e=>e.link,sortable:!0},{name:"text",headerStyle:"display: none",style:"display: none",label:"Descrizione",align:"left",field:e=>e.text,sortable:!0},{name:"is_interesting",label:"",align:"left",field:e=>e.is_interesting,sortable:!0}]}},computed:o()(o()({},Object(u["c"])(["houses"])),{},{lastUpdate(){return q["a"].formatDate(new Date(Math.max(...this.houses.map((e=>new Date(e.updated))))),"DD/MM/YYYY - HH:mm")}}),mounted(){this.$store.dispatch("getHouses"),setInterval((()=>this.$store.dispatch("getHouses")),1e4)},methods:{formatCurrency(e){return null!==e?e.toLocaleString("it-IT",{style:"currency",currency:"EUR"}):"N.D."},price_mqColor(e){return e<500?"text-green-10":e<1e3?"text-green-5":e<1250?"text-yellow":e<1500?"text-red":e>=1500?"text-indigo-10":void 0}}},w=x,v=(l("76a5"),l("eaac")),I=l("db86"),k=l("9c40"),C=l("05c0"),M=l("0016"),z=Object(m["a"])(w,i,r,!1,null,null,null),F=z.exports;_()(z,"components",{QTable:v["a"],QInput:b["a"],QTd:I["a"],QBtn:k["a"],QTooltip:C["a"],QIcon:M["a"]});var Q={name:"Index",components:{Table:F}},S=Q,P=l("9989"),N=Object(m["a"])(S,a,n,!1,null,null,null);t["default"]=N.exports;_()(N,"components",{QPage:P["a"]})}}]);