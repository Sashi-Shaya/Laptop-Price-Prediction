from flask import Flask, render_template, request
import pickle
import numpy as np

# setup application
app = Flask(__name__)

def prediction(lst):
    filename = 'model/predictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value

@app.route('/', methods=['POST', 'GET'])
def index():
    # return "Hello World"
    pred_value = 0
    if request.method == 'POST':
        ram = request.form['ram']
        weight = request.form['weight']
        company = request.form['company']
        typename = request.form['typename']
        opsys = request.form['opsys']
        cpu = request.form['cpuname']
        gpu = request.form['gpuname']
        touchscreen = request.form.getlist('touchscreen')
        ips = request.form.getlist('ips')
        
        feature_list = []

        feature_list.append(int(ram))
        feature_list.append(float(weight))
        feature_list.append(len(touchscreen))
        feature_list.append(len(ips))

        company_list = ['acer','apple','asus','dell','hp','lenovo','msi','other','toshiba']
        typename_list = ['2in1convertible','gaming','netbook','notebook','ultrabook','workstation']
        opsys_list = ['linux','mac','other','windows']
        cpu_list = ['amd_a10_9600p', 'amd_a10_9620p', 'amd_a10_9620p_2', 'amd_a12_9700p', 'amd_a12_9720p', 'amd_a12_9720p_2', 'amd_a4_7210', 'amd_a6_7310', 'amd_a6_9220', 'amd_a6_9220_2', 'amd_a6_9220_3', 'amd_a8_7410', 'amd_a9_9410', 'amd_a9_9420', 'amd_a9_9420_2', 'amd_a9_9420_3', 'amd_e_6110', 'amd_e_7110', 'amd_e_9000', 'amd_e_9000e', 'amd_e2_6110', 'amd_e2_9000', 'amd_e2_9000e', 'amd_fx_8800p', 'amd_fx_9830p', 'amd_ryzen_1600', 'amd_ryzen_1700', 'intel_atom_x5_z8350', 'intel_atom_z8350', 'intel_atom_x5_z8300', 'intel_atom_x5_z8350_2', 'intel_celeron_3205u', 'intel_celeron_3855u', 'intel_celeron_n3050', 'intel_celeron_n3060', 'intel_celeron_n3060_2', 'intel_celeron_n3350', 'intel_celeron_n3350_2', 'intel_celeron_n3350_3', 'intel_atom_x5_z8550', 'intel_celeron_n3160', 'intel_celeron_n3450', 'intel_celeron_n3710', 'intel_core_m_1_1', 'intel_core_m_1_2', 'intel_core_m_6y30', 'intel_core_m_6y54', 'intel_core_m_6y75', 'intel_core_m_7y30', 'intel_core_m_m3_6y30', 'intel_core_m_m7_6y75', 'intel_core_m_m3_1_2', 'intel_core_m_m3_7y30', 'intel_core_m_m7_6y75', 'intel_core_i3_6006u_2_0', 'intel_core_i3_6006u_2_2', 'intel_core_i3_6006u_2', 'intel_core_i3_6100u_2_1', 'intel_core_i3_6100u_2_3', 'intel_core_i3_7100u_2_4', 'intel_core_i3_7130u_2_7', 'intel_core_i5_1_3', 'intel_core_i5_1_6', 'intel_core_i5_1_8', 'intel_core_i5_2_0', 'intel_core_i5_2_3', 'intel_core_i5_2_9', 'intel_core_i5_3_1', 'intel_core_i5_6200u_2_3', 'intel_core_i5_6260u_1_8', 'intel_core_i5_6300hq_2_3', 'intel_core_i5_6300u_2_4', 'intel_core_i5_6440hq_2_6', 'intel_core_i5_7200u_2_50', 'intel_core_i5_7200u_2_5', 'intel_core_i5_7200u_2_70', 'intel_core_i5_7200u_2_7', 'intel_core_i5_7300hq_2_5', 'intel_core_i5_7300u_2_6', 'intel_core_i5_7440hq_2_8', 'intel_core_i5_7500u_2_7', 'intel_core_i5_7y54_1_2', 'intel_core_i5_7y57_1_2', 'intel_core_i5_8250u_1_6', 'intel_core_i7_2_2', 'intel_core_i7_2_7', 'intel_core_i7_2_8', 'intel_core_i7_2_9', 'intel_core_i7_6500u_2_50', 'intel_core_i7_6500u_2_5', 'intel_core_i7_6560u_2_2', 'intel_core_i7_6600u_2_6', 'intel_core_i7_6700hq_2_6', 'intel_core_i7_6820hk_2_7', 'intel_core_i7_6820hq_2_7', 'intel_core_i7_6920hq_2_9', 'intel_core_i7_7500u_2_5', 'intel_core_i7_7500u_2_7', 'intel_core_i7_7560u_2_4', 'intel_core_i7_7600u_2_8', 'intel_core_i7_7660u_2_5', 'intel_pentium_dual_core_4405u_2_1', 'intel_core_i7_7700hq_2_7', 'intel_core_i7_7700hq_2_8', 'intel_core_i7_7820hk_2_9', 'intel_core_i7_7820hq_2_9', 'intel_core_i7_7y75_1_3', 'intel_core_i7_8550u_1_8', 'intel_core_i7_8650u_1_9', 'intel_pentium_dual_core_4405y_1_5', 'intel_pentium_dual_core_n4200_1_1', 'intel_pentium_quad_core_n3700_1_6', 'intel_pentium_quad_core_n3710_1_6', 'intel_pentium_quad_core_n4200_1_1', 'intel_xeon_e3_1505m_v6_3', 'intel_xeon_e3_1535m_v5_2_9', 'intel_xeon_e3_1535m_v6_3_1', 'samsung_cortex_a72_a53_2_0']
        gpu_list = ['amd_firepro_w4190m', 'amd_firepro_w4190m_2', 'amd_firepro_w5130m', 'amd_firepro_w6150m', 'amd_r17m_m1_70', 'amd_r4_graphics', 'amd_radeon_520', 'amd_radeon_530', 'amd_radeon_540', 'amd_radeon_pro_455', 'amd_radeon_pro_555', 'amd_radeon_pro_560', 'amd_radeon_r2', 'amd_radeon_r2_graphics', 'amd_radeon_r5_m330', 'amd_radeon_r3', 'amd_radeon_r4', 'amd_radeon_r4_graphics', 'amd_radeon_r5', 'amd_radeon_r5_430', 'amd_radeon_r5_520', 'amd_radeon_r5_m315', 'amd_radeon_r5_m420', 'amd_radeon_r5_m420x', 'amd_radeon_r5_m430', 'amd_radeon_r7', 'amd_radeon_r7_graphics', 'amd_radeon_r7_m360', 'amd_radeon_r7_m365x', 'amd_radeon_r7_m440', 'amd_radeon_r7_m445', 'amd_radeon_r7_m460', 'amd_radeon_r7_m465', 'amd_radeon_r9_m385', 'amd_radeon_rx_540', 'amd_radeon_rx_550', 'amd_radeon_rx_560', 'amd_radeon_rx_580', 'arm_mali_t860_mp4', 'intel_graphics_620', 'intel_hd_graphics', 'intel_hd_graphics_400', 'intel_hd_graphics_405', 'intel_hd_graphics_500', 'intel_hd_graphics_505', 'intel_hd_graphics_510', 'intel_hd_graphics_515', 'intel_hd_graphics_520', 'intel_hd_graphics_530', 'intel_hd_graphics_5300', 'intel_hd_graphics_540', 'intel_hd_graphics_6000', 'intel_hd_graphics_615', 'intel_hd_graphics_620', 'intel_hd_graphics_630', 'intel_iris_graphics_540', 'intel_iris_graphics_550', 'intel_iris_plus_graphics_640', 'intel_iris_plus_graphics_650', 'intel_iris_pro_graphics', 'intel_uhd_graphics_620', 'nvidia_gtx_980_sli', 'nvidia_geforce_150mx', 'nvidia_geforce_920', 'nvidia_geforce_920m', 'nvidia_geforce_920mx', 'nvidia_geforce_930m', 'nvidia_geforce_930mx', 'nvidia_geforce_940m', 'nvidia_geforce_940mx', 'nvidia_geforce_960m', 'nvidia_geforce_gt_940mx', 'nvidia_geforce_gtx_1050', 'nvidia_geforce_gtx_1050_ti', 'nvidia_geforce_gtx_1050m', 'nvidia_geforce_gtx_1050ti', 'nvidia_geforce_gtx_1060', 'nvidia_geforce_gtx_1070', 'nvidia_geforce_gtx_1070m', 'nvidia_geforce_gtx_1080', 'nvidia_geforce_gtx_930mx', 'nvidia_quadro_m1000m', 'nvidia_geforce_gtx_940m', 'nvidia_geforce_gtx_940mx', 'nvidia_geforce_gtx_950m', 'nvidia_geforce_gtx_960', 'nvidia_geforce_gtx_960m', 'nvidia_geforce_gtx_965m', 'nvidia_geforce_gtx_970m', 'nvidia_geforce_gtx_980', 'nvidia_geforce_gtx_980m', 'nvidia_geforce_gtx_1050_ti', 'nvidia_geforce_gtx_1060', 'nvidia_geforce_gtx_1080', 'nvidia_geforce_mx130', 'nvidia_geforce_mx150', 'nvidia_quadro_3000m', 'nvidia_quadro_m1200', 'nvidia_quadro_m2000m', 'nvidia_quadro_m2200', 'nvidia_quadro_m2200m', 'nvidia_quadro_m3000m', 'nvidia_quadro_m500m', 'nvidia_quadro_m520m', 'nvidia_quadro_m620', 'nvidia_quadro_m620m', 'nvidia_geforce_gtx_965m', 'nvidia_geforce_gtx_970m', 'nvidia_geforce_gtx_980', 'nvidia_geforce_gtx_980m']
        # for item in company_list:
        #     if item == company:
        #         feature_list.append(1)
        #     else:
        #         feature_list.append(0)

        def traverse_list(lst, value):
            for item in lst:
                if item == value:
                    feature_list.append(1)
                else:
                    feature_list.append(0)
        
        traverse_list(company_list, company)
        traverse_list(typename_list, typename)
        traverse_list(opsys_list, opsys)
        traverse_list(cpu_list, cpu)
        traverse_list(gpu_list, gpu)

        pred_value = prediction(feature_list)
        pred_value = np.round(pred_value[0],2)*309.35

    return render_template('index.html', pred_value=pred_value)


if __name__ == '__main__':
    app.run(debug=True)