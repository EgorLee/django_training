from django.shortcuts import render
from .models import Order
from .forms import OrderForms
from django.views.generic import DetailView
from cms.models import CmsSlider
from cms.models import MetaTags
from price.models import PriceCard, PriceTable
from .teiegram import sendTelegram


def first_page(request):
    slider_list = CmsSlider.objects.all()
    form = OrderForms()
    all_meta = MetaTags.objects.first()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    list_price = [price.pt_new_price for price in price_table]
    site, seo, ppc = map(int, list_price)
    site_ppc = site + ppc
    total = site + ppc + seo
    dct_obj = {'slider_list': slider_list,
               "site_ppc": site_ppc,
               'total': total,
               "site": site,
               "seo": seo,
               "ppc": ppc,
               'pc_1': pc_1,
               'pc_2': pc_2,
               'pc_3': pc_3,
               'price_table': price_table,
               'form': form,
               'all_meta': all_meta}
    return render(request, './index.html', dct_obj)


def thanks_page(request):
    if request.POST:
        object_list = Order.objects.all()
        name = request.POST['name']
        phone = request.POST['phone']
        sendTelegram(name, phone)
        elem = Order(order_name=name, order_phone=phone)
        elem.save()
        return render(request, "./thanks_page.html", {"object_list": object_list, "name": name, 'phone': phone})
    else:
        return render(request, "./thanks_page.html")


def custom_404(request, exception):
    return render(request, '404.html', {'exception': exception}, status=404)