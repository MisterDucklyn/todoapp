var sil_butonlari = document.querySelectorAll('.delete-data')

sil_butonlari.forEach(sil_butonu=>{
    sil_butonu.addEventListener('click',function(e){
        var silinsinmi = confirm('Silməy istədiyindən əminsən ?')
        if(!silinsinmi){
            e.preventDefault()
        }
    })
})

var hamisini_sil = document.querySelector('.delete-all-data')
hamisini_sil.addEventListener('click',function(e){
        var silinsinmi = confirm('Bütün planını silməy istədiyindən əminsən ?')
        if(!silinsinmi){
            e.preventDefault()
        }
    })

var duzelt_butonlari = document.querySelectorAll('.edit-data')
duzelt_butonlari.forEach(duzelt_butonu=>{
    duzelt_butonu.addEventListener('click',function(e){
        var editEdirsen = confirm('Dəyişməy istədiyindən əminsən ?')
        if(editEdirsen){
            var data_id = duzelt_butonu.getAttribute('data-id')
            var input_value = duzelt_butonu.previousElementSibling.value
            document.getElementById('hiddenid').value = data_id
            document.getElementById('description').value=input_value
            duzelt_butonu.parentElement.remove()
        } else{
            e.preventDefault()
        }
        
    })
})

setInterval(() => {
    var alert_qutular = document.querySelectorAll('.alert-box')
    alert_qutular.forEach(alert_qutusu => {
        alert_qutusu.remove()
    })
}, 5000);
