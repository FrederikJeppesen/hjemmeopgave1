# HST.py: Read in hearthstone data, manually scraped from online. 

import pandas as pd 
import numpy as np 

def read_data(): 
    '''read_data()
        OUTPUTS: 
            dat: (pandas df) winrate matrix
            playrates: (pandas df) empirically observed play ratesl
    '''
    playrates = pd.DataFrame([
        ('No Minion Mage',12.89),
        ('Control Warlock',12.10),
        ('Face Hunter',12.02),
        ('Secret Paladin',7.89),
        ('Rush Warrior',4.13),
        ('Secret Libram Paladin',4.08),
        ('Midrange Demon Hunter',3.67),
        ('Control Priest',3.44),
        ('Token Druid',3.19),
        ('Aggro Paladin',2.81),
        ('Spell Damage Mage',2.10),
        ('Ping Mage',1.94),
        ('Miracle Rogue',1.93),
        ('Other Mage',1.75),
        ('Heal Priest',1.62),
        ('Control Warrior',1.57),
        ('Rally Priest',1.49),
        ('Aggro Shaman',1.35)],
                             columns = ['deck', 'playrate'])

    dat = [('No Minion Mage', 'Control Warlock', 53.60,  98857),
        ('No Minion Mage', 'Face Hunter', 32.11,  94130),
        ('No Minion Mage', 'Secret Paladin', 32.57,  62587),
        ('No Minion Mage', 'Rush Warrior', 46.10,  32558),
        ('No Minion Mage', 'Secret Libram Paladin', 42.82, 32515),
        ('No Minion Mage', 'Midrange Demon Hunter', 46.95, 28190),
        ('No Minion Mage', 'Control Priest', 62.81,  27632),
        ('No Minion Mage', 'Token Druid', 45.08,  25074),
        ('No Minion Mage', 'Aggro Paladin', 47.00,  21341),
        ('No Minion Mage', 'Spell Damage Mage', 60.63, 16242),
        ('No Minion Mage', 'Ping Mage', 65.20,  15780),
        ('No Minion Mage', 'Miracle Rogue', 54.55,  15101),
        ('No Minion Mage', 'Other Mage', 67.58,  12211),
        ('No Minion Mage', 'Heal Priest', 62.43,  13328),
        ('No Minion Mage', 'Control Warrior', 66.92,  12241),
        ('No Minion Mage', 'Rally Priest', 69.09,  11865),
        ('No Minion Mage', 'Aggro Shaman', 52.07,  10273),
        ('No Minion Mage', 'Deathrattle Demon Hunter', 44.98, 10106),
        ('Control Warlock', 'No Minion Mage', 46.38,  98857),
        ('Control Warlock', 'Face Hunter', 35.36, 90867),
        ('Control Warlock', 'Secret Paladin', 36.80, 56924),
        ('Control Warlock', 'Rush Warrior', 50.90, 29591),
        ('Control Warlock', 'Secret Libram Paladin', 56.63,  31824),
        ('Control Warlock', 'Midrange Demon Hunter', 35.78,  25784),
        ('Control Warlock', 'Control Priest', 80.01, 21508),
        ('Control Warlock', 'Token Druid', 49.02, 22489),
        ('Control Warlock', 'Aggro Paladin', 48.05, 18285),
        ('Control Warlock', 'Spell Damage Mage', 49.72,  13103),
        ('Control Warlock', 'Ping Mage', 49.03, 13437),
        ('Control Warlock', 'Miracle Rogue', 52.19, 13392),
        ('Control Warlock', 'Other Mage', 64.53, 16909),
        ('Control Warlock', 'Heal Priest', 79.49, 9990),
        ('Control Warlock', 'Control Warrior', 65.51, 9633),
        ('Control Warlock', 'Rally Priest', 76.77, 10253),
        ('Control Warlock', 'Aggro Shaman', 40.12, 9649),
        ('Control Warlock', 'Deathrattle Demon Hunter', 37.80,  9648),
        ('Face Hunter', 'No Minion Mage', 67.66,  94130),
        ('Face Hunter', 'Control Warlock', 64.54, 90867),
        ('Face Hunter', 'Secret Paladin', 40.80, 56132),
        ('Face Hunter', 'Rush Warrior', 43.90, 29847),
        ('Face Hunter', 'Secret Libram Paladin', 38.78,  32011),
        ('Face Hunter', 'Midrange Demon Hunter', 60.74,  27722),
        ('Face Hunter', 'Control Priest', 44.54, 24696),
        ('Face Hunter', 'Token Druid', 48.20, 22961),
        ('Face Hunter', 'Aggro Paladin', 43.11, 19349),
        ('Face Hunter', 'Spell Damage Mage', 66.66,  15009),
        ('Face Hunter', 'Ping Mage', 76.48, 15205),
        ('Face Hunter', 'Miracle Rogue', 60.29, 13410),
        ('Face Hunter', 'Other Mage', 74.32, 10994),
        ('Face Hunter', 'Heal Priest', 40.64, 11377),
        ('Face Hunter', 'Control Warrior', 56.83, 11777),
        ('Face Hunter', 'Rally Priest', 47.98, 10912),
        ('Face Hunter', 'Aggro Shaman', 68.09, 10136),
        ('Face Hunter', 'Deathrattle Demon Hunter', 63.29,  9767),
        ('Secret Paladin', 'No Minion Mage', 67.42,  62587),
        ('Secret Paladin', 'Control Warlock', 63.18, 56924),
        ('Secret Paladin', 'Face Hunter', 58.99, 56132),
        ('Secret Paladin', 'Rush Warrior', 45.49, 22836),
        ('Secret Paladin', 'Secret Libram Paladin', 53.62,  17996),
        ('Secret Paladin', 'Midrange Demon Hunter', 74.49,  16247),
        ('Secret Paladin', 'Control Priest', 60.03, 17685),
        ('Secret Paladin', 'Token Druid', 61.47, 14880),
        ('Secret Paladin', 'Aggro Paladin', 54.81, 15272),
        ('Secret Paladin', 'Spell Damage Mage', 68.81,  10386),
        ('Secret Paladin', 'Ping Mage', 73.88, 8329),
        ('Secret Paladin', 'Miracle Rogue', 59.11, 9363),
        ('Secret Paladin', 'Other Mage', 73.13, 6139),
        ('Secret Paladin', 'Heal Priest', 57.26, 8031),
        ('Secret Paladin', 'Control Warrior', 72.47, 6958),
        ('Secret Paladin', 'Rally Priest', 69.03, 6175),
        ('Secret Paladin', 'Aggro Shaman', 75.25, 5909),
        ('Secret Paladin', 'Deathrattle Demon Hunter', 60.63,  5889),
        ('Rush Warrior', 'No Minion Mage', 53.88,  32558),
        ('Rush Warrior', 'Control Warlock', 49.08, 29591),
        ('Rush Warrior', 'Face Hunter', 55.87, 29847),
        ('Rush Warrior', 'Secret Paladin', 54.49, 22836),
        ('Rush Warrior', 'Secret Libram Paladin', 51.59,  9592),
        ('Rush Warrior', 'Midrange Demon Hunter', 63.71,  8302),
        ('Rush Warrior', 'Control Priest', 47.91, 9099),
        ('Rush Warrior', 'Token Druid', 60.67, 7825),
        ('Rush Warrior', 'Aggro Paladin', 50.77, 8250),
        ('Rush Warrior', 'Spell Damage Mage', 69.67,  5122),
        ('Rush Warrior', 'Ping Mage', 72.11, 4379),
        ('Rush Warrior', 'Miracle Rogue', 68.17, 5210),
        ('Rush Warrior', 'Other Mage', 67.39, 3092),
        ('Rush Warrior', 'Heal Priest', 49.19, 4139),
        ('Rush Warrior', 'Control Warrior', 62.21, 3390),
        ('Rush Warrior', 'Rally Priest', 60.47, 3292),
        ('Rush Warrior', 'Aggro Shaman', 67.00, 2988),
        ('Rush Warrior', 'Deathrattle Demon Hunter', 58.68,  3047),
        ('Secret Libram Paladin', 'No Minion Mage', 57.16, 32515),
        ('Secret Libram Paladin', 'Control Warlock', 43.36,  31824),
        ('Secret Libram Paladin', 'Face Hunter', 61.07,  32011),
        ('Secret Libram Paladin', 'Secret Paladin', 46.37,  17996),
        ('Secret Libram Paladin', 'Rush Warrior', 48.40,  9592),
        ('Secret Libram Paladin', 'Midrange Demon Hunter', 72.70, 9108),
        ('Secret Libram Paladin', 'Control Priest', 53.40,  8172),
        ('Secret Libram Paladin', 'Token Druid', 55.33,  7605),
        ('Secret Libram Paladin', 'Aggro Paladin', 54.68,  5972),
        ('Secret Libram Paladin', 'Spell Damage Mage', 63.55, 4525),
        ('Secret Libram Paladin', 'Ping Mage', 67.63,  5089),
        ('Secret Libram Paladin', 'Miracle Rogue', 57.80,  4358),
        ('Secret Libram Paladin', 'Other Mage', 68.39,  4066),
        ('Secret Libram Paladin', 'Heal Priest', 52.79,  3955),
        ('Secret Libram Paladin', 'Control Warrior', 68.56,  3862),
        ('Secret Libram Paladin', 'Rally Priest', 63.33,  3677),
        ('Secret Libram Paladin', 'Aggro Shaman', 73.16,  3462),
        ('Secret Libram Paladin', 'Deathrattle Demon Hunter', 64.54, 3548),
        ('Midrange Demon Hunter', 'No Minion Mage', 53.03, 28190),
        ('Midrange Demon Hunter', 'Control Warlock', 64.21,  25784),
        ('Midrange Demon Hunter', 'Face Hunter', 39.08,  27722),
        ('Midrange Demon Hunter', 'Secret Paladin', 25.50,  16247),
        ('Midrange Demon Hunter', 'Rush Warrior', 36.28,  8302),
        ('Midrange Demon Hunter', 'Secret Libram Paladin', 27.29, 9108),
        ('Midrange Demon Hunter', 'Control Priest', 57.64,  7404),
        ('Midrange Demon Hunter', 'Token Druid', 34.78,  7055),
        ('Midrange Demon Hunter', 'Aggro Paladin', 29.49,  5954),
        ('Midrange Demon Hunter', 'Spell Damage Mage', 59.79, 5034),
        ('Midrange Demon Hunter', 'Ping Mage', 68.03,  4577),
        ('Midrange Demon Hunter', 'Miracle Rogue', 48.44,  4223),
        ('Midrange Demon Hunter', 'Other Mage', 61.00,  4093),
        ('Midrange Demon Hunter', 'Heal Priest', 51.20,  3615),
        ('Midrange Demon Hunter', 'Control Warrior', 64.51,  3841),
        ('Midrange Demon Hunter', 'Rally Priest', 50.34,  3492),
        ('Midrange Demon Hunter', 'Aggro Shaman', 57.74,  3420),
        ('Midrange Demon Hunter', 'Deathrattle Demon Hunter', 36.70, 2861),
        ('Control Priest', 'No Minion Mage', 37.18,  27632),
        ('Control Priest', 'Control Warlock', 19.98, 21508),
        ('Control Priest', 'Face Hunter', 55.42, 24696),
        ('Control Priest', 'Secret Paladin', 39.95, 17685),
        ('Control Priest', 'Rush Warrior', 52.08, 9099),
        ('Control Priest', 'Secret Libram Paladin', 46.59,  8172),
        ('Control Priest', 'Midrange Demon Hunter', 42.35,  7404),
        ('Control Priest', 'Token Druid', 51.97, 7128),
        ('Control Priest', 'Aggro Paladin', 48.17, 6267),
        ('Control Priest', 'Spell Damage Mage', 43.66,  4363),
        ('Control Priest', 'Ping Mage', 40.60, 3694),
        ('Control Priest', 'Miracle Rogue', 48.33, 4144),
        ('Control Priest', 'Other Mage', 54.60, 4463),
        ('Control Priest', 'Heal Priest', 55.46, 2854),
        ('Control Priest', 'Control Warrior', 49.75, 2820),
        ('Control Priest', 'Rally Priest', 56.78, 2858),
        ('Control Priest', 'Aggro Shaman', 47.68, 2699),
        ('Control Priest', 'Deathrattle Demon Hunter', 48.94,  2603),
        ('Token Druid', 'No Minion Mage', 54.91,  25074),
        ('Token Druid', 'Control Warlock', 50.97, 22489),
        ('Token Druid', 'Face Hunter', 51.71, 22961),
        ('Token Druid', 'Secret Paladin', 38.52, 14880),
        ('Token Druid', 'Rush Warrior', 39.32, 7825),
        ('Token Druid', 'Secret Libram Paladin', 44.66,  7605),
        ('Token Druid', 'Midrange Demon Hunter', 65.21,  7055),
        ('Token Druid', 'Control Priest', 48.02, 7128),
        ('Token Druid', 'Aggro Paladin', 48.34, 5413),
        ('Token Druid', 'Spell Damage Mage', 55.17,  4319),
        ('Token Druid', 'Ping Mage', 58.84, 3839),
        ('Token Druid', 'Miracle Rogue', 57.01, 3590),
        ('Token Druid', 'Other Mage', 63.89, 3357),
        ('Token Druid', 'Heal Priest', 49.80, 3000),
        ('Token Druid', 'Control Warrior', 52.34, 3156),
        ('Token Druid', 'Rally Priest', 58.56, 2778),
        ('Token Druid', 'Aggro Shaman', 51.39, 2722),
        ('Token Druid', 'Deathrattle Demon Hunter', 66.86,  2472),
        ('Aggro Paladin', 'No Minion Mage', 52.97,  21341),
        ('Aggro Paladin', 'Control Warlock', 51.94, 18285),
        ('Aggro Paladin', 'Face Hunter', 56.73, 19349),
        ('Aggro Paladin', 'Secret Paladin', 45.18, 15272),
        ('Aggro Paladin', 'Rush Warrior', 49.22, 8250),
        ('Aggro Paladin', 'Secret Libram Paladin', 45.31,  5972),
        ('Aggro Paladin', 'Midrange Demon Hunter', 70.50,  5954),
        ('Aggro Paladin', 'Control Priest', 51.82, 6267),
        ('Aggro Paladin', 'Token Druid', 51.65, 5413),
        ('Aggro Paladin', 'Spell Damage Mage', 58.00,  4098),
        ('Aggro Paladin', 'Ping Mage', 65.74, 3010),
        ('Aggro Paladin', 'Miracle Rogue', 53.32, 3522),
        ('Aggro Paladin', 'Other Mage', 62.05, 2712),
        ('Aggro Paladin', 'Heal Priest', 52.39, 2878),
        ('Aggro Paladin', 'Control Warrior', 65.21, 2524),
        ('Aggro Paladin', 'Rally Priest', 59.45, 2368),
        ('Aggro Paladin', 'Aggro Shaman', 68.15, 2173),
        ('Aggro Paladin', 'Deathrattle Demon Hunter', 62.11,  2117),
        ('Spell Damage Mage', 'No Minion Mage', 39.34, 16242),
        ('Spell Damage Mage', 'Control Warlock', 50.23,  13103),
        ('Spell Damage Mage', 'Face Hunter', 33.14,  15009),
        ('Spell Damage Mage', 'Secret Paladin', 31.17,  10386),
        ('Spell Damage Mage', 'Rush Warrior', 30.30,  5122),
        ('Spell Damage Mage', 'Secret Libram Paladin', 36.44,  4525),
        ('Spell Damage Mage', 'Midrange Demon Hunter', 40.16,  5034),
        ('Spell Damage Mage', 'Control Priest', 56.33,  4363),
        ('Spell Damage Mage', 'Token Druid', 44.82,  4319),
        ('Spell Damage Mage', 'Aggro Paladin', 41.99,  4098),
        ('Spell Damage Mage', 'Ping Mage', 52.85,  2766),
        ('Spell Damage Mage', 'Miracle Rogue', 46.49,  2568),
        ('Spell Damage Mage', 'Other Mage', 55.05,  2879),
        ('Spell Damage Mage', 'Heal Priest', 55.72,  2019),
        ('Spell Damage Mage', 'Control Warrior', 59.62,  2046),
        ('Spell Damage Mage', 'Rally Priest', 58.70,  2015),
        ('Spell Damage Mage', 'Aggro Shaman', 44.91,  1870),
        ('Spell Damage Mage', 'Deathrattle Demon Hunter', 36.86, 1625),
        ('Ping Mage', 'No Minion Mage', 34.77,  15780),
        ('Ping Mage', 'Control Warlock', 50.94, 13437),
        ('Ping Mage', 'Face Hunter', 23.34, 15205),
        ('Ping Mage', 'Secret Paladin', 26.11, 8329),
        ('Ping Mage', 'Rush Warrior', 27.88, 4379),
        ('Ping Mage', 'Secret Libram Paladin', 32.36,  5089),
        ('Ping Mage', 'Midrange Demon Hunter', 31.96,  4577),
        ('Ping Mage', 'Control Priest', 59.39, 3694),
        ('Ping Mage', 'Token Druid', 41.15, 3839),
        ('Ping Mage', 'Aggro Paladin', 34.25, 3010),
        ('Ping Mage', 'Spell Damage Mage', 47.14,  2766),
        ('Ping Mage', 'Miracle Rogue', 43.98, 2260),
        ('Ping Mage', 'Other Mage', 57.53, 2555),
        ('Ping Mage', 'Heal Priest', 55.80, 1939),
        ('Ping Mage', 'Control Warrior', 57.73, 1914),
        ('Ping Mage', 'Rally Priest', 55.37, 2167),
        ('Ping Mage', 'Aggro Shaman', 40.33, 1815),
        ('Ping Mage', 'Deathrattle Demon Hunter', 32.15,  1757),
        ('Miracle Rogue', 'No Minion Mage', 45.43,  15101),
        ('Miracle Rogue', 'Control Warlock', 47.80, 13392),
        ('Miracle Rogue', 'Face Hunter', 39.49, 13410),
        ('Miracle Rogue', 'Secret Paladin', 40.87, 9363),
        ('Miracle Rogue', 'Rush Warrior', 31.80, 5210),
        ('Miracle Rogue', 'Secret Libram Paladin', 42.17,  4358),
        ('Miracle Rogue', 'Midrange Demon Hunter', 51.55,  4223),
        ('Miracle Rogue', 'Control Priest', 51.64, 4144),
        ('Miracle Rogue', 'Token Druid', 42.98, 3590),
        ('Miracle Rogue', 'Aggro Paladin', 46.67, 3522),
        ('Miracle Rogue', 'Spell Damage Mage', 53.50,  2568),
        ('Miracle Rogue', 'Ping Mage', 55.97, 2260),
        ('Miracle Rogue', 'Other Mage', 55.48, 1849),
        ('Miracle Rogue', 'Heal Priest', 50.70, 1917),
        ('Miracle Rogue', 'Control Warrior', 53.52, 1788),
        ('Miracle Rogue', 'Rally Priest', 54.73, 1754),
        ('Miracle Rogue', 'Aggro Shaman', 49.28, 1532),
        ('Miracle Rogue', 'Deathrattle Demon Hunter', 44.57,  1402),
        ('Other Mage', 'No Minion Mage', 32.29,  12211),
        ('Other Mage', 'Control Warlock', 35.40, 16909),
        ('Other Mage', 'Face Hunter', 25.36, 10994),
        ('Other Mage', 'Secret Paladin', 26.76, 6139),
        ('Other Mage', 'Rush Warrior', 32.60, 3092),
        ('Other Mage', 'Secret Libram Paladin', 31.60,  4066),
        ('Other Mage', 'Midrange Demon Hunter', 38.92,  4093),
        ('Other Mage', 'Control Priest', 45.35, 4463),
        ('Other Mage', 'Token Druid', 36.10, 3357),
        ('Other Mage', 'Aggro Paladin', 37.86, 2712),
        ('Other Mage', 'Spell Damage Mage', 44.87,  2879),
        ('Other Mage', 'Ping Mage', 42.38, 2555),
        ('Other Mage', 'Miracle Rogue', 44.34, 1849),
        ('Other Mage', 'Heal Priest', 50.26, 2638),
        ('Other Mage', 'Control Warrior', 49.82, 2605),
        ('Other Mage', 'Rally Priest', 51.77, 2285),
        ('Other Mage', 'Aggro Shaman', 45.19, 1591),
        ('Other Mage', 'Deathrattle Demon Hunter', 32.03,  1211),
        ('Heal Priest', 'No Minion Mage', 37.52,  13328),
        ('Heal Priest', 'Control Warlock', 20.50, 9990),
        ('Heal Priest', 'Face Hunter', 59.27, 11377),
        ('Heal Priest', 'Secret Paladin', 42.73, 8031),
        ('Heal Priest', 'Rush Warrior', 50.80, 4139),
        ('Heal Priest', 'Secret Libram Paladin', 47.20,  3955),
        ('Heal Priest', 'Midrange Demon Hunter', 48.76,  3615),
        ('Heal Priest', 'Control Priest', 44.49, 2854),
        ('Heal Priest', 'Token Druid', 50.20, 3000),
        ('Heal Priest', 'Aggro Paladin', 47.60, 2878),
        ('Heal Priest', 'Spell Damage Mage', 44.27,  2019),
        ('Heal Priest', 'Ping Mage', 44.09, 1939),
        ('Heal Priest', 'Miracle Rogue', 49.29, 1917),
        ('Heal Priest', 'Other Mage', 49.65, 2638),
        ('Heal Priest', 'Control Warrior', 55.10, 1441),
        ('Heal Priest', 'Rally Priest', 51.62, 1447),
        ('Heal Priest', 'Aggro Shaman', 50.87, 1378),
        ('Heal Priest', 'Deathrattle Demon Hunter', 56.86,  1245),
        ('Control Warrior', 'No Minion Mage', 33.06,  12241),
        ('Control Warrior', 'Control Warlock', 34.48, 9633),
        ('Control Warrior', 'Face Hunter', 43.07, 11777),
        ('Control Warrior', 'Secret Paladin', 27.52, 6958),
        ('Control Warrior', 'Rush Warrior', 37.78, 3390),
        ('Control Warrior', 'Secret Libram Paladin', 31.43,  3862),
        ('Control Warrior', 'Midrange Demon Hunter', 35.48,  3841),
        ('Control Warrior', 'Control Priest', 50.24, 2820),
        ('Control Warrior', 'Token Druid', 47.65, 3156),
        ('Control Warrior', 'Aggro Paladin', 34.78, 2524),
        ('Control Warrior', 'Spell Damage Mage', 40.37,  2046),
        ('Control Warrior', 'Ping Mage', 42.26, 1914),
        ('Control Warrior', 'Miracle Rogue', 46.47, 1788),
        ('Control Warrior', 'Other Mage', 50.13, 2605),
        ('Control Warrior', 'Heal Priest', 44.89, 1441),
        ('Control Warrior', 'Rally Priest', 48.04, 1511),
        ('Control Warrior', 'Aggro Shaman', 46.00, 1415),
        ('Control Warrior', 'Deathrattle Demon Hunter', 31.93,  1262),
        ('Rally Priest', 'No Minion Mage', 30.89,  11865),
        ('Rally Priest', 'Control Warlock', 23.22, 10253),
        ('Rally Priest', 'Face Hunter', 51.99, 10912),
        ('Rally Priest', 'Secret Paladin', 30.96, 6175),
        ('Rally Priest', 'Rush Warrior', 39.52, 3292),
        ('Rally Priest', 'Secret Libram Paladin', 36.60,  3677),
        ('Rally Priest', 'Midrange Demon Hunter', 49.65,  3492),
        ('Rally Priest', 'Control Priest', 43.21, 2858),
        ('Rally Priest', 'Token Druid', 41.43, 2778),
        ('Rally Priest', 'Aggro Paladin', 40.54, 2368),
        ('Rally Priest', 'Spell Damage Mage', 41.29,  2015),
        ('Rally Priest', 'Ping Mage', 44.62, 2167),
        ('Rally Priest', 'Miracle Rogue', 45.26, 1754),
        ('Rally Priest', 'Other Mage', 48.05, 2285),
        ('Rally Priest', 'Heal Priest', 48.37, 1447),
        ('Rally Priest', 'Control Warrior', 51.95, 1511),
        ('Rally Priest', 'Aggro Shaman', 44.04, 1385),
        ('Rally Priest', 'Deathrattle Demon Hunter', 50.70,  1211),
        ('Aggro Shaman', 'No Minion Mage', 47.92,  10273),
        ('Aggro Shaman', 'Control Warlock', 59.87, 9649),
        ('Aggro Shaman', 'Face Hunter', 31.77, 10136),
        ('Aggro Shaman', 'Secret Paladin', 24.72, 5909),
        ('Aggro Shaman', 'Rush Warrior', 32.99, 2988),
        ('Aggro Shaman', 'Secret Libram Paladin', 26.83,  3462),
        ('Aggro Shaman', 'Midrange Demon Hunter', 42.25,  3420),
        ('Aggro Shaman', 'Control Priest', 52.31, 2699),
        ('Aggro Shaman', 'Token Druid', 48.60, 2722),
        ('Aggro Shaman', 'Aggro Paladin', 31.79, 2173),
        ('Aggro Shaman', 'Spell Damage Mage', 55.08,  1870),
        ('Aggro Shaman', 'Ping Mage', 59.66, 1815),
        ('Aggro Shaman', 'Miracle Rogue', 50.71, 1532),
        ('Aggro Shaman', 'Other Mage', 54.74, 1591),
        ('Aggro Shaman', 'Heal Priest', 49.12, 1378),
        ('Aggro Shaman', 'Control Warrior', 53.99, 1415),
        ('Aggro Shaman', 'Rally Priest', 55.88, 1385),
        ('Aggro Shaman', 'Deathrattle Demon Hunter', 38.27,  1168),
        ('Deathrattle Demon Hunter', 'No Minion Mage', 55.00, 10106),
        ('Deathrattle Demon Hunter', 'Control Warlock', 62.19,  9648),
        ('Deathrattle Demon Hunter', 'Face Hunter', 36.56,  9767),
        ('Deathrattle Demon Hunter', 'Secret Paladin', 39.36,  5889),
        ('Deathrattle Demon Hunter', 'Rush Warrior', 41.31,  3047),
        ('Deathrattle Demon Hunter', 'Secret Libram Paladin', 35.45, 3548),
        ('Deathrattle Demon Hunter', 'Midrange Demon Hunter', 63.29, 2861),
        ('Deathrattle Demon Hunter', 'Control Priest', 51.05,  2603),
        ('Deathrattle Demon Hunter', 'Token Druid', 33.13,  2472),
        ('Deathrattle Demon Hunter', 'Aggro Paladin', 37.88,  2117),
        ('Deathrattle Demon Hunter', 'Spell Damage Mage', 63.13, 1625),
        ('Deathrattle Demon Hunter', 'Ping Mage', 67.84,  1757),
        ('Deathrattle Demon Hunter', 'Miracle Rogue', 55.42,  1402),
        ('Deathrattle Demon Hunter', 'Other Mage', 67.87,  1211),
        ('Deathrattle Demon Hunter', 'Heal Priest', 43.13,  1245),
        ('Deathrattle Demon Hunter', 'Control Warrior', 68.06,  1262),
        ('Deathrattle Demon Hunter', 'Rally Priest', 49.29,  1211),
        ('Deathrattle Demon Hunter', 'Aggro Shaman', 61.72,  1168),
        ('Poison Rogue', 'No Minion Mage', 54.99,  10404),
        ('Poison Rogue', 'Control Warlock', 62.12, 8744),
        ('Poison Rogue', 'Face Hunter', 23.71, 9067),
        ('Poison Rogue', 'Secret Paladin', 15.11, 5643),
        ('Poison Rogue', 'Rush Warrior', 40.26, 3204),
        ('Poison Rogue', 'Secret Libram Paladin', 19.06,  3026),
        ('Poison Rogue', 'Midrange Demon Hunter', 37.90,  2810),
        ('Poison Rogue', 'Control Priest', 58.89, 2705),
        ('Poison Rogue', 'Token Druid', 21.79, 2367),
        ('Poison Rogue', 'Aggro Paladin', 27.22, 2332),
        ('Poison Rogue', 'Spell Damage Mage', 57.24,  1829),
        ('Poison Rogue', 'Ping Mage', 60.78, 1655),
        ('Poison Rogue', 'Miracle Rogue', 55.12, 1453),
        ('Poison Rogue', 'Other Mage', 58.85, 1203),
        ('Poison Rogue', 'Heal Priest', 43.91, 1241),
        ('Poison Rogue', 'Control Warrior', 52.39, 1252),
        ('Poison Rogue', 'Rally Priest', 47.46, 1203),
        ('Poison Rogue', 'Aggro Shaman', 44.76, 1088),
        ('Poison Rogue', 'Deathrattle Demon Hunter', 37.29,  1027),
        ('Other Hunter', 'No Minion Mage', 36.56,  8230),
        ('Other Hunter', 'Control Warlock', 42.70, 10153),
        ('Other Hunter', 'Face Hunter', 26.04, 7778),
        ('Other Hunter', 'Secret Paladin', 24.17, 4938),
        ('Other Hunter', 'Rush Warrior', 28.34, 2406),
        ('Other Hunter', 'Secret Libram Paladin', 27.59,  2805),
        ('Other Hunter', 'Midrange Demon Hunter', 42.49,  2513),
        ('Other Hunter', 'Control Priest', 38.09, 2785),
        ('Other Hunter', 'Token Druid', 23.50, 2336),
        ('Other Hunter', 'Aggro Paladin', 29.41, 1955),
        ('Other Hunter', 'Spell Damage Mage', 47.23,  1721),
        ('Other Hunter', 'Ping Mage', 49.35, 1710),
        ('Other Hunter', 'Miracle Rogue', 40.57, 1284),
        ('Other Hunter', 'Other Mage', 52.43, 1373),
        ('Other Hunter', 'Heal Priest', 39.06, 1459),
        ('Other Hunter', 'Control Warrior', 51.59, 1603),
        ('Other Hunter', 'Rally Priest', 39.95, 1289),
        ('Other Hunter', 'Aggro Shaman', 42.84, 1027),
        ('Other Hunter', 'Deathrattle Demon Hunter', 40.56,  885),
        ('Lifesteal Demon Hunter', 'No Minion Mage', 42.06, 8834),
        ('Lifesteal Demon Hunter', 'Control Warlock', 57.58,  7202),
        ('Lifesteal Demon Hunter', 'Face Hunter', 45.60,  7128),
        ('Lifesteal Demon Hunter', 'Secret Paladin', 18.17,  5359),
        ('Lifesteal Demon Hunter', 'Rush Warrior', 35.25,  3046),
        ('Lifesteal Demon Hunter', 'Secret Libram Paladin', 26.38, 2293),
        ('Lifesteal Demon Hunter', 'Midrange Demon Hunter', 39.22, 2228),
        ('Lifesteal Demon Hunter', 'Control Priest', 56.87,  2518),
        ('Lifesteal Demon Hunter', 'Token Druid', 46.58,  2170),
        ('Lifesteal Demon Hunter', 'Aggro Paladin', 27.79,  2069),
        ('Lifesteal Demon Hunter', 'Spell Damage Mage', 49.24, 1521),
        ('Lifesteal Demon Hunter', 'Ping Mage', 61.42,  1081),
        ('Lifesteal Demon Hunter', 'Miracle Rogue', 49.18,  1354),
        ('Lifesteal Demon Hunter', 'Other Mage', 56.32,  861),
        ('Lifesteal Demon Hunter', 'Heal Priest', 53.94,  977),
        ('Lifesteal Demon Hunter', 'Control Warrior', 50.93,  909),
        ('Lifesteal Demon Hunter', 'Rally Priest', 47.96,  959),
        ('Lifesteal Demon Hunter', 'Aggro Shaman', 49.61,  784),
        ('Lifesteal Demon Hunter', 'Deathrattle Demon Hunter', 32.73, 721),
        ('Murloc Shaman', 'No Minion Mage', 43.92,  7939),
        ('Murloc Shaman', 'Control Warlock', 43.70, 7639),
        ('Murloc Shaman', 'Face Hunter', 51.83, 7667),
        ('Murloc Shaman', 'Secret Paladin', 45.75, 4292),
        ('Murloc Shaman', 'Rush Warrior', 27.62, 2136),
        ('Murloc Shaman', 'Secret Libram Paladin', 42.00,  2619),
        ('Murloc Shaman', 'Midrange Demon Hunter', 52.11,  2433),
        ('Murloc Shaman', 'Control Priest', 42.11, 2206),
        ('Murloc Shaman', 'Token Druid', 59.92, 2016),
        ('Murloc Shaman', 'Aggro Paladin', 45.69, 1534),
        ('Murloc Shaman', 'Spell Damage Mage', 53.89,  1475),
        ('Murloc Shaman', 'Ping Mage', 60.47, 1480),
        ('Murloc Shaman', 'Miracle Rogue', 52.42, 1070),
        ('Murloc Shaman', 'Other Mage', 57.00, 1214),
        ('Murloc Shaman', 'Heal Priest', 47.79, 1044),
        ('Murloc Shaman', 'Control Warrior', 41.80, 1129),
        ('Murloc Shaman', 'Rally Priest', 57.47, 1084),
        ('Murloc Shaman', 'Aggro Shaman', 54.19, 965),
        ('Murloc Shaman', 'Deathrattle Demon Hunter', 47.92,  820),
        ('Other Warrior', 'No Minion Mage', 36.16,  6570),
        ('Other Warrior', 'Control Warlock', 26.95, 8821),
        ('Other Warrior', 'Face Hunter', 37.46, 4948),
        ('Other Warrior', 'Secret Paladin', 32.71, 3289),
        ('Other Warrior', 'Rush Warrior', 36.19, 1978),
        ('Other Warrior', 'Secret Libram Paladin', 34.87,  1864),
        ('Other Warrior', 'Midrange Demon Hunter', 43.73,  1859),
        ('Other Warrior', 'Control Priest', 34.99, 2326),
        ('Other Warrior', 'Token Druid', 36.93, 1519),
        ('Other Warrior', 'Aggro Paladin', 35.16, 1402),
        ('Other Warrior', 'Spell Damage Mage', 46.00,  1315),
        ('Other Warrior', 'Ping Mage', 46.61, 1328),
        ('Other Warrior', 'Miracle Rogue', 46.56, 932),
        ('Other Warrior', 'Other Mage', 48.02, 1316),
        ('Other Warrior', 'Heal Priest', 39.12, 1296),
        ('Other Warrior', 'Control Warrior', 44.08, 1268),
        ('Other Warrior', 'Rally Priest', 44.16, 1037),
        ('Other Warrior', 'Aggro Shaman', 54.30, 744),
        ('Other Warrior', 'Deathrattle Demon Hunter', 42.73,  606)]

    dat = pd.DataFrame(dat, columns=['deck1', 'deck2', 'winrate', 'num_games'])

    I = dat.deck1.isin(playrates.deck) & dat.deck2.isin(playrates.deck)
    dat = dat.loc[I].copy()

    dat = dat.pivot(index='deck1', columns='deck2', values='winrate')

    # diagonal not in dataset 
    dat.fillna(50, inplace=True)
    
    return dat, playrates