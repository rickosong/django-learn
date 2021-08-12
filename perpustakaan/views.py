from django.shortcuts import render, redirect
from perpustakaan.models import Buku
from perpustakaan.forms import FormBuku

# Create your views here.

def buku(request):
    buku = Buku.objects.all()
    
    konteks = {
        'books' : buku
    }

    return render(request, 'buku.html', konteks)

def penerbit(request):
    return render(request, 'penerbit.html')

def TambahBuku(request):

    form = FormBuku()
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/buku/')

    konteks= {'form':form}
    return render(request, 'tambah-buku.html', konteks)

def ubahBuku(request, pk):
    buku = Buku.objects.get(id=pk)
    form = FormBuku(instance=buku)
    if request.method == 'POST':
        form = FormBuku(request.POST, instance=buku)
        if form.is_valid():
            form.save()
            return redirect('/buku/')

    konteks = {'form':form}
    return render(request, 'tambah-buku.html', konteks)

def hapusBuku(request, pk):
    buku = Buku.objects.get(id=pk)
    if request.method == 'POST':
        buku.delete()
        return redirect('/buku/')
        
    konteks = {'item':buku}
    return render(request, 'hapus.html', konteks)
