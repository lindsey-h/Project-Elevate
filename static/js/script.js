"use strict";

var myEvents = [
  { 
    id: "required-id-1",
    name: "New Year", 
    date: "Wed Aug 28 2021 00:00:00 GMT-0800 (Pacific Standard Time)", 
    type: "holiday", 
    everyYear: true 
  },
  { 
    id: "required-id-2",
    name: "Valentine's Day", 
    date: "Wed Aug 28 2021 00:00:00 GMT-0800 (Pacific Standard Time)", 
    type: "holiday", 
    everyYear: true,
    color: "#222"
  },
  { 
    id: "required-id-3",
    name: "Custom Date", 
    badge: "08/03 - 08/05",
    date: ["August/03/2021", "August/05/2021"],
    description: "Description here",
    type: "event", 
  }
]

$('#evoCalendar').evoCalendar({
  calendarEvents: myEvents,
  todayHighlight: true,
  sidebarToggler: true,
  sidebarDisplayDefault: false,
});