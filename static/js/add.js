// Code for Date Field
let today = new Date();
let dd = String(today.getDate()).padStart(2, '0');
let mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
let yyyy = today.getFullYear();

// today = dd + '-' + mm + '-' + yyyy;
today = yyyy + '-' + mm + '-' + dd;
document.getElementById('date').value = today;

// Function for calculating NET WEIGHT - 1st
function gt_weight_calc() {
    let gross_weight = parseInt(document.getElementById('gross_weight').value);
    let tier_weight = parseInt(document.getElementById('tier_weight').value);

    // to make sure that they are numbers
    if (!gross_weight) {
        gross_weight = 0;
    }
    if (!tier_weight) {
        tier_weight = 0;
    }

    let gt_weight = document.getElementById('gt_weight');
    gt_weight.value = gross_weight - tier_weight;
}

// Function for calculating BORA WEIGHT - 2nd
function bags_weight_calc() {
    let jute75 = parseFloat(document.getElementById('jute75').value);
    let jute40 = parseFloat(document.getElementById('jute40').value) * 0.7;
    let plastic40 = parseFloat(document.getElementById('plastic40').value) * 0.25;

    // to make sure that they are numbers
    if (!jute75) {
        jute75 = 0;
    }
    if (!jute40) {
        jute40 = 0;
    }
    if (!plastic40) {
        plastic40 = 0;
    }

    let bags_weight = document.getElementById('bags_weight');
    bags_weight.value = Math.ceil(jute75 + jute40 + plastic40);
}

// Function for calculating SUDDH WEIGHT - 3rd
function net_weight_calc() {
    let gt_weight = document.getElementById('gt_weight').value;
    let bags_weight = document.getElementById('bags_weight').value;

    let net_weight = document.getElementById('net_weight');
    net_weight.value = ((gt_weight - bags_weight) / 100).toFixed(2);
}

// Function for 1st, 2nd and 3rd
function trio_call() {
    gt_weight_calc();
    bags_weight_calc();
    net_weight_calc();
}

// Function for calculating LOADING AMOUNT
function load() {
    let jute75 = parseInt(document.getElementById('jute75').value);
    let jute40 = parseInt(document.getElementById('jute40').value);
    let plastic40 = parseInt(document.getElementById('plastic40').value);

    // to make sure that they are numbers
    if (!jute75) {
        jute75 = 0;
    }
    if (!jute40) {
        jute40 = 0;
    }
    if (!plastic40) {
        plastic40 = 0;
    }

    document.getElementById('loading').value = Math.ceil((jute75 * 5) + (jute40 * 2.5) + (plastic40 * 2.5));
}

// Function for calculating UNLOADING AMOUNT
function unload() {
    let jute75_1 = parseInt(document.getElementById('jute75').value);
    let jute40_1 = parseInt(document.getElementById('jute40').value);
    let plastic40_1 = parseInt(document.getElementById('plastic40').value);

    // to make sure that they are numbers
    if (!jute75_1) {
        jute75_1 = 0;
    }
    if (!jute40_1) {
        jute40_1 = 0;
    }
    if (!plastic40_1) {
        plastic40_1 = 0;
    }

    document.getElementById('unloading').value = Math.ceil((jute75_1 * 5) + (jute40_1 * 2.5) + (plastic40_1 * 2.5));
}

// Function for SETTING LOADING TOTAL 0
function load_total() {
    if (document.getElementById('loading_farmer').checked === true) {
        document.getElementById('loading').value = 0;
    }
}

// Function for SETTING UNLOADING TOTAL 0
function unload_total() {
    if (document.getElementById('unloading_farmer').checked === true) {
        document.getElementById('unloading').value = 0;
    }
}

// Function for calculating GROSS TOTAL
function gross_total_calc() {
    let net_weight = parseFloat(document.getElementById('net_weight').value);
    let rate = parseFloat(document.getElementById('rate').value);
    let gross_total = document.getElementById('gross_total')
        gross_total.value = Math.floor(net_weight * rate);
}

// Function for calculating DEDUCTION
function deduct() {
    let deduction = document.getElementById('deduction');
    let gross_total = parseInt(document.getElementById('gross_total').value);

    if (document.getElementById('deduction0').checked === true) {
        deduction.value = 0;
    } else if (document.getElementById('deduction1').checked === true) {
        deduction.value = Math.ceil((gross_total * (1 / 100)));
    } else if (document.getElementById('deduction1_5').checked === true) {
        deduction.value = Math.ceil((gross_total * (1.5 / 100)));
    }
}

// Function for calculating HEMALI
function hemali_calc() {
    let loading_value = parseInt(document.getElementById('loading').value);
    let unloading_value = parseInt(document.getElementById('unloading').value);

    document.getElementById('lo_unlo_charges').value = loading_value + unloading_value;
}

// Function for calculating OUR VEHICLE RENT
function vehicle_rent_calc() {
    let net_weight = parseFloat(document.getElementById('net_weight').value);
    let our_vehicle_charges = parseFloat(document.getElementById('our_vehicle_charges').value);

    document.getElementById('our_vehicle_charges_total').value = Math.ceil(net_weight * our_vehicle_charges);
}

// Function for calculating AGENT COMMISSION
function agent_commission_cal() {
    let net_weight = parseFloat(document.getElementById('net_weight').value);
    let agent_commission = document.getElementById('agent_commission_total');

    if (document.getElementById('0').checked === true) {
        agent_commission.value = 0;
    } else if (document.getElementById('2').checked === true) {
        agent_commission.value = Math.floor(net_weight * 2);
    } else if (document.getElementById('3').checked === true) {
        agent_commission.value = Math.floor(net_weight * 3);
    } else if (document.getElementById('4').checked === true) {
        agent_commission.value = Math.floor(net_weight * 4);
    } else if (document.getElementById('5').checked === true) {
        agent_commission.value = Math.floor(net_weight * 5);
    }

}

// Function for calculating NET TOTAL
function net_total_calc() {
    let gross_total = parseInt(document.getElementById('gross_total').value);
    let deduction = parseInt(document.getElementById('deduction').value);
    let wb_charges = parseInt(document.getElementById('wb_charges').value);
    let lo_unlo = parseInt(document.getElementById('lo_unlo_charges').value);
    let vehicle_rent_charges = parseInt(document.getElementById('our_vehicle_charges_total').value);
    let agent_commission = parseInt(document.getElementById('agent_commission_total').value);
    let other_exp = parseInt(document.getElementById('other_exp').value);
    let advance = parseInt(document.getElementById('advance').value);

    let net_total = document.getElementById('net_total');

    net_total.value = (gross_total + agent_commission - (deduction + wb_charges + lo_unlo + vehicle_rent_charges + other_exp + advance));
}