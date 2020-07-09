var lst =[]
$('.list-item').each(function(){
    lst.push({
        region:$(this).find('tt').text(),
        context:$(this).find('list-item-detail').text(),
    })

})
