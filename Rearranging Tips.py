# from opentrons import types

# metadata
metadata = {
    'protocolName': 'Rearranging Tips',
    'author': 'M.Pauwels <marthe.pauwels@pathosense.com>',
    'apiLevel': '2.10'
}

def run(protocol):
    # load labware and pipettes
    trBG_1 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 1)
    trBG_2 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 4)
    trBG_3 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 7)
    trA_1 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 2)
    trA_2 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 3)
    trA_3 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 5)
    trA_4 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 6)
    trA_5 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 8)
    trA_6 = protocol.load_labware('opentrons_96_filtertiprack_200ul', 9)
    P300_single = protocol.load_instrument('p300_single_gen2', mount='left')

    # define linked tipracks eg. trBG_1 --> trA_1 and trA_2
    series_1 = [trBG_1, trA_1, trA_2]
    series_2 = [trBG_2, trA_3, trA_4]
    series_3 = [trBG_3, trA_5, trA_6]
    all_series = [series_1, series_2, series_3]
    
    # target row A of a tiprack
    # P300_single.pick_up_tip(trBG_1.rows()[0])
    
    # adjust speed to faster (default 400 mm/s)
    default_speed = 1600

    # iterate over series (linked tipracks)
    for serie in all_series:
        trBG = serie[0]
        trA_A = serie[1]
        trA_B = serie[2]
        
        # for i from position A1 tot A12 tiprack1 (= range 12 and .row()[0]) pick up tip and drop in tiprack2&3 row A1 to A12 
        for i in range(12): 
            tip_position = trBG.rows()[0][i]
            P300_single.pick_up_tip(tip_position)
            P300_single.drop_tip(trA_A.rows()[0][i])
        
        for i in range(12): 
            tip_position = trBG.rows()[7][i]
            P300_single.pick_up_tip(tip_position)
            P300_single.drop_tip(trA_B.rows()[0][i])
        
    ''' for i in range(1):
           if i == 0:
               pick_up_position = 0
               bring_to = trA_A 
           if i == 1:
               pick_up_position = 7
               bring_to = trA_B

           for i in range(12): 
               tip_position = trBG.rows()[pick_up_position][i]
               P300_single.pick_up_tip(tip_position)
               P300_single.drop_tip(bring_to.rows()[0][i])
    '''
