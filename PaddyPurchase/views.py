from django.shortcuts import render, redirect
from .models import PaddyPurchase
from django.http import FileResponse
from fpdf import FPDF


# Create your views here.

def index(request):
    return render(request, 'dashboard.html')


# View for DATA ENTRY FORM
def add_record(request):
    dbRecords = PaddyPurchase.objects.all()
    var_ref_no = PaddyPurchase.objects.latest('ref_no')
    var_ref_no_value = var_ref_no.ref_no + 1
    dbRecords_dict = {
        'PaddyPurchase': dbRecords,
        'ref_no': var_ref_no_value
    }
    return render(request, 'add_record.html', dbRecords_dict)


# View for SAVING RECORD
def save_record(request):
    if request.method == 'POST':
        var_ref_no = request.POST.get('ref_no')
        var_token_no = request.POST.get('token_no')
        var_agent_name = request.POST.get('agent_name')
        var_trip_no = request.POST.get('trip_no')
        var_date = request.POST.get('date')
        var_vehicle_no = request.POST.get('vehicle_no')
        var_jute75 = request.POST.get('jute75')
        var_jute40 = request.POST.get('jute40')
        var_plastic40 = request.POST.get('plastic40')
        var_farmer_name = request.POST.get('farmer_name')
        var_farmer_address = request.POST.get('farmer_address')
        var_farmer_mob = request.POST.get('farmer_mob')
        var_gross_weight = request.POST.get('gross_weight')
        var_tier_weight = request.POST.get('tier_weight')
        var_gt_weight = request.POST.get('gt_weight')
        var_bags_weight = request.POST.get('bags_weight')
        var_net_weight = request.POST.get('net_weight')
        var_loading = request.POST.get('loading')
        var_unloading = request.POST.get('unloading')
        var_unloading_point = request.POST.get('unloading_point')
        var_wb_operator = request.POST.get('wb_operator')
        var_rate = request.POST.get('rate')
        var_jute_bags = request.POST.get('jute_bags')
        var_gross_total = request.POST.get('gross_total')
        var_deduction = request.POST.get('deduction')
        var_wb_charges = request.POST.get('wb_charges')
        var_lo_unlo_charges = request.POST.get('lo_unlo_charges')
        var_our_vehicle_charges_total = request.POST.get('our_vehicle_charges_total')
        var_agent_commission = request.POST.get('agent_commission_total')
        var_other_exp = request.POST.get('other_exp')
        var_other_exp_remark = request.POST.get('other_exp_remark')
        var_advance = request.POST.get('advance')
        var_net_total = request.POST.get('net_total')

        var_data_save = PaddyPurchase(
            ref_no=var_ref_no,
            token_no=var_token_no,
            agent_name=var_agent_name,
            trip_no=var_trip_no,
            date=var_date,
            vehicle_no=var_vehicle_no,
            jute75=var_jute75,
            jute40=var_jute40,
            plastic40=var_plastic40,
            farmer_name=var_farmer_name,
            farmer_address=var_farmer_address,
            farm_mob=var_farmer_mob,
            gross_weight=var_gross_weight,
            tier_weight=var_tier_weight,
            gt_weight=var_gt_weight,
            bags_weight=var_bags_weight,
            net_weight=var_net_weight,
            loading=var_loading,
            unloading=var_unloading,
            unloading_point=var_unloading_point,
            wb_operator=var_wb_operator,
            rate=var_rate,
            jute_bags=var_jute_bags,
            gross_total=var_gross_total,
            deduction=var_deduction,
            wb_charges=var_wb_charges,
            lo_unlo_charges=var_lo_unlo_charges,
            our_vehicle_charges=var_our_vehicle_charges_total,
            agent_commission=var_agent_commission,
            other_exp=var_other_exp,
            other_exp_remark=var_other_exp_remark,
            advance=var_advance,
            net_total=var_net_total)

        var_data_save.save()
    return redirect(add_record)


# View for DOWNLOADING REPORTS PAGE
def reports(request):
    dbRecords = PaddyPurchase.objects.all()
    context = {
        'PaddyPurchase': dbRecords,
    }
    return render(request, 'reports.html', context)


# For downloading Records in PDF File
def download_pdf(request):
    if request.method == 'POST':
        # For Getting Reference Number AKA Primary Key
        var_ref_no_for_download = request.POST.get('ref_no_for_download')
        # Designate the model
        dbRecords = PaddyPurchase.objects.get(pk=var_ref_no_for_download)

        # Constructor
        pdf = FPDF(orientation='L', unit='mm', format='A4')
        pdf.set_top_margin(margin=5)
        pdf.set_left_margin(margin=5)
        pdf.set_right_margin(margin=5)
        pdf.set_auto_page_break(auto=bool, margin=3)
        pdf.add_page()
        pdf.set_font('Courier', style='', size=12)

        # Template DRAFTING - *****
        pdf.cell(90, 8, 'RECEIPT', 'LTR', 1, 'C')
        pdf.dashed_line(10, 12, 100, 12, 1, 1)
        pdf.cell(45, 7, 'Ref No.: ', 'L', 0, 'L'), pdf.cell(45, 7, str(dbRecords.ref_no), 'R', 1, 'L')
        pdf.cell(45, 7, 'Token No.: ', 'L', 0, 'L'), pdf.cell(45, 7, str(dbRecords.token_no), 'R', 1, 'L')
        pdf.cell(45, 7, 'Agent Name: ', 'L', 0, 'L'), pdf.cell(45, 7, str(dbRecords.agent_name), 'R', 1, 'L')
        pdf.cell(45, 7, 'Trip No.: ', 'L', 0, 'L'), pdf.cell(45, 7, str(dbRecords.trip_no), 'R', 1, 'L')
        pdf.cell(45, 7, 'Date: ', 'L', 0, 'L'), pdf.cell(45, 7, str(dbRecords.date), 'R', 1, 'L')
        pdf.cell(45, 7, 'Vehicle No.: ', 'L', 0, 'L'), pdf.cell(45, 7, str(dbRecords.vehicle_no), 'R', 1, 'L')
        pdf.cell(45, 7, 'Bora: ', 'L', 0, 'L'), pdf.cell(45, 7, str(dbRecords.jute75), 'R', 1, 'L')
        pdf.cell(45, 7, 'Katta: ', 'L', 0, 'L'), pdf.cell(45, 7, str(dbRecords.jute40), 'R', 1, 'L')
        pdf.cell(45, 7, 'Plastic: ', 'L', 0, 'L'), pdf.cell(45, 7, str(dbRecords.plastic40), 'R', 1, 'L')
        pdf.cell(45, 7, 'Farmer Name: ', 'L', 0, 'L'), pdf.cell(45, 7, str(dbRecords.farmer_name), 'R', 1, 'L')
        pdf.cell(45, 7, 'Farmer Address: ', 'L', 0, 'L'), pdf.cell(45, 7, str(dbRecords.farmer_address), 'R', 1, 'L')
        pdf.cell(45, 7, 'Farmer Mob. No.: ', 'L', 0, 'L'), pdf.cell(45, 7, str(dbRecords.farm_mob), 'R', 1, 'L')
        pdf.cell(45, 7, 'Gross Weight: ', 'L', 0, 'L'), pdf.cell(45, 7, str(dbRecords.gross_weight) + ' Kg.', 'R', 1,
                                                                 'L')
        pdf.cell(45, 7, 'Tier Weight: ', 'L', 0, 'L'), pdf.cell(45, 7, str(dbRecords.tier_weight) + ' Kg.', 'R', 1, 'L')
        pdf.cell(45, 7, 'Gross Tier Diff.: ', 'L', 0, 'L'), pdf.cell(45, 7, str(dbRecords.gt_weight) + ' Kg.', 'R', 1,
                                                                     'L')
        pdf.cell(45, 7, 'Bora Weight: ', 'L', 0, 'L'), pdf.cell(45, 7, str(dbRecords.bags_weight) + ' Kg.', 'R', 1, 'L')
        pdf.cell(45, 7, 'Net Weight: ', 'L', 0, 'L'), pdf.cell(45, 7, str(dbRecords.net_weight) + ' Qntl.', 'R', 1, 'L')
        pdf.cell(45, 7, 'Loading Amt.: ', 'L', 0, 'L'), pdf.cell(45, 7, 'Rs. ' + str(dbRecords.loading), 'R', 1, 'L')
        pdf.cell(45, 7, 'Unloading Amt.: ', 'L', 0, 'L'), pdf.cell(45, 7, 'Rs. ' + str(dbRecords.unloading), 'R', 1,
                                                                   'L')
        pdf.cell(45, 7, 'WB Charges: ', 'L', 0, 'L'), pdf.cell(45, 7, 'Rs. ' + str(dbRecords.wb_charges), 'R', 1, 'L')
        pdf.cell(45, 7, 'Unloading Point: ', 'L', 0, 'L'), pdf.cell(45, 7, str(dbRecords.unloading_point), 'R', 1, 'L')
        pdf.cell(45, 7, 'WB Operator: ', 'L', 0, 'L'), pdf.cell(45, 7, 'Mr. ' + str(dbRecords.wb_operator), 'R', 1, 'L')
        pdf.cell(45, 7, 'Rate: ', 'L', 0, 'L'), pdf.cell(45, 7, 'Rs. ' + str(dbRecords.rate), 'R', 1, 'L')
        pdf.cell(45, 7, 'Bags Status: ', 'L', 0, 'L'), pdf.cell(45, 7, str(dbRecords.jute_bags), 'R', 1, 'L')
        pdf.cell(45, 22, 'Signature', 'LB', 0, 'L'), pdf.cell(45, 22, 'Farmer Signature', 'RB', 1, 'L')

        # Saving & Exporting PDF
        pdf.output('report.pdf', 'F')

        return FileResponse(open('report.pdf', 'rb'), as_attachment=True, content_type='application/pdf')
    else:
        redirect(reports)
