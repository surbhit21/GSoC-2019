//genesis
// kkit Version 11 flat dumpfile

// Saved on 100
include kkit {argv 1}
FASTDT = 0.001
SIMDT = 0.001
CONTROLDT = 0.1
PLOTDT = 0.1
MAXTIME = 100
TRANSIENT_TIME = 2
VARIABLE_DT_FLAG = 0
DEFAULT_VOL = 1.05292121233e-15
VERSION = 11.0 
setfield /file/modpath value ~/scripts/modules
kparms

//genesis
initdump -version 3 -ignoreorphans 1
simobjdump table input output alloced step_mode stepsize x y z
simobjdump xtree path script namemode sizescale
simobjdump xcoredraw xmin xmax ymin ymax
simobjdump xtext editable
simobjdump xgraph xmin xmax ymin ymax overlay
simobjdump xplot pixflags script fg ysquish do_slope wy
simobjdump group xtree_fg_req xtree_textfg_req plotfield expanded movealone \
  link savename file version md5sum mod_save_flag x y z
simobjdump geometry size dim shape outside xtree_fg_req xtree_textfg_req x y z
simobjdump kpool DiffConst CoInit Co n nInit mwt nMin vol slave_enable \
  geomname xtree_fg_req xtree_textfg_req x y z
simobjdump kreac kf kb notes xtree_fg_req xtree_textfg_req x y z
simobjdump kenz CoComplexInit CoComplex nComplexInit nComplex vol k1 k2 k3 \
  keepconc usecomplex notes xtree_fg_req xtree_textfg_req link x y z
simobjdump stim level1 width1 delay1 level2 width2 delay2 baselevel trig_time \
  trig_mode notes xtree_fg_req xtree_textfg_req is_running x y z
simobjdump xtab input output alloced step_mode stepsize notes editfunc \
  xtree_fg_req xtree_textfg_req baselevel last_x last_y is_running x y z
simobjdump kchan perm gmax Vm is_active use_nernst notes xtree_fg_req \
  xtree_textfg_req x y z
simobjdump transport input output alloced step_mode stepsize dt delay clock \
  kf xtree_fg_req xtree_textfg_req x y z
simobjdump proto x y z
simundump geometry /kinetics/geometry 0 1.05292121233e-15 3 sphere  "" white black 4 2 0
simundump group /kinetics/Compartment 0 blue green x 0 0 "" defaultfile \
  defaultfile.g 0 0 0 1 2 0
simundump group /kinetics/Gs 0 blue green x 0 0 "" defaultfile \
  defaultfile.g 0 0 0 1 2 0
simundump group /kinetics/cAMP_grp 0 blue green x 0 0 "" defaultfile \
  defaultfile.g 0 0 0 1 2 0
simundump group /kinetics/PKA 0 blue green x 0 0 "" defaultfile \
  defaultfile.g 0 0 0 1 2 0
simundump kpool /kinetics/Gs/Epinephrine 0 0.0 0 0 0 634084.052901 0 0 634084.052901 0 /kinetics/geometry 50 black 2330 0 0
simundump kpool /kinetics/Gs/B2AR 0 0.0 0 0 0 62765.0410381 0 0 634084.052901 0 /kinetics/geometry 23 black 1876 -1317 0
simundump kpool /kinetics/Gs/Epi_B2AR 0 0.0 0 0 0 0.0 0 0 634084.052901 0 /kinetics/geometry 6 black 3002 -1325 0
simundump kpool /kinetics/Gs/GDP_Gs_ABG 0 0.0 0 0 0 1138726.10566 0 0 634084.052901 0 /kinetics/geometry 23 black 2577 -2777 0
simundump kpool /kinetics/Gs/B2AR_GDP_Gs_ABG 0 0.0 0 0 0 0.0 0 0 634084.052901 0 /kinetics/geometry 8 black 0 -2732 0
simundump kpool /kinetics/Gs/Epi_B2AR_GDP_Gs_ABG 0 0.0 0 0 0 0.0 0 0 634084.052901 0 /kinetics/geometry 23 black 2068 -3553 0
simundump kpool /kinetics/Gs/Gs_BG 0 0.0 0 0 0 0.0 0 0 634084.052901 0 /kinetics/geometry 19 black 4667 -2875 0
simundump kpool /kinetics/Gs/GTP_GsA 0 0.0 0 0 0 0.0 0 0 634084.052901 0 /kinetics/geometry 23 black 5107 -1267 0
simundump kpool /kinetics/Gs/GDP_GsA 0 0.0 0 0 0 0.0 0 0 634084.052901 0 /kinetics/geometry 6 black 6117 -3599 0
simundump kpool /kinetics/cAMP_grp/AC1 0 0.0 0 0 0 6265.73224296 0 0 634084.052901 0 /kinetics/geometry 42 black 8617 -4766 0
simundump kpool /kinetics/cAMP_grp/GsA_AC1 0 0.0 0 0 0 0.0 0 0 634084.052901 0 /kinetics/geometry 19 black 8210 -3482 0
simundump kpool /kinetics/cAMP_grp/cAMP 0 0.0 0 0 0 0.0 0 0 634084.052901 0 /kinetics/geometry 63 black 8506 -2249 0
simundump kpool /kinetics/cAMP_grp/cAMP_PDE 0 0.0 0 0 0 317042.026452 0 0 634084.052901 0 /kinetics/geometry 55 black 9627 -882 0
simundump kpool /kinetics/cAMP_grp/ATP 0 0.0 0 0 0 105399255.07 0 0 634084.052901 4 /kinetics/geometry 6 black 9609 -2209 0
simundump kpool /kinetics/cAMP_grp/AMP 0 0.0 0 0 0 634084052.901 0 0 634084.052901 4 /kinetics/geometry 23 black 8164 -1176 0
simundump kpool /kinetics/Gs/Isoproterenol 0 0.0 0 0 0 6340840.52901 0 0 634084.052901 0 /kinetics/geometry 54 black 106 -171 0
simundump kpool /kinetics/cAMP_grp/AC2 0 0.0 0 0 0 8691.63480541 0 0 634084.052901 0 /kinetics/geometry 23 black 9848 -4690 0
simundump kpool /kinetics/cAMP_grp/GsA_AC2 0 0.0 0 0 0 0.0 0 0 634084.052901 0 /kinetics/geometry 25 black 9803 -3482 0
simundump kpool /kinetics/cAMP_grp/cAMP_PDE_P 0 0.0 0 0 0 0.0 0 0 634084.052901 0 /kinetics/geometry 50 black 8540 -352 0
simundump kpool /kinetics/PKA/R2C2 0 0.0 0 0 0 317042.026697 0 0 634084.052901 0 /kinetics/geometry 3 black 242 -6316 0
simundump kpool /kinetics/PKA/cAMP_R2C2 0 0.0 0 0 0 0.0 0 0 634084.052901 0 /kinetics/geometry 53 black 1134 -6304 0
simundump kpool /kinetics/PKA/cAMP2_R2C2 0 0.0 0 0 0 0.0 0 0 634084.052901 0 /kinetics/geometry 53 black 2823 -6330 0
simundump kpool /kinetics/PKA/cAMP3_R2C2 0 0.0 0 0 0 0.0 0 0 634084.052901 0 /kinetics/geometry 55 black 4530 -6318 0
simundump kpool /kinetics/PKA/cAMP4_R2C2 0 0.0 0 0 0 0.0 0 0 634084.052901 0 /kinetics/geometry 24 black 6187 -6341 0
simundump kpool /kinetics/PKA/cAMP4_R2C 0 0.0 0 0 0 0.0 0 0 634084.052901 0 /kinetics/geometry 27 black 4780 -6904 0
simundump kpool /kinetics/PKA/cAMP4_R2 0 0.0 0 0 0 0.0 0 0 634084.052901 0 /kinetics/geometry 63 black 3438 -6899 0
simundump kpool /kinetics/PKA/PKA_Active 0 0.0 0 0 0 0.0 0 0 634084.052901 0 /kinetics/geometry 26 black 4178 -7976 0
simundump kpool /kinetics/PKA/PKA_Inhibitor 0 0.0 0 0 0 317042.02649 0 0 634084.052901 0 /kinetics/geometry 23 black 1621 -6952 0
simundump kpool /kinetics/PKA/Inhibited_PKA 0 0.0 0 0 0 0.0 0 0 634084.052901 0 /kinetics/geometry 19 black 1197 -8000 0
simundump kreac /kinetics/Gs/Reac_Epi_B2AR 0 2.66689734514e-07 0.0601018161373 "" white black 2771 -605 0
simundump kreac /kinetics/Gs/Reac_B2AR_GDP_G_ABG 0 2.15696278254e-07 0.0932611603566 "" white black 1242 -1875 0
simundump kreac /kinetics/Gs/Reac_Epi_B2AR_GDP_G_ABG 0 1.50474554791e-05 0.10008713592 "" white black 2557 -1811 0
simundump kreac /kinetics/Gs/Reac_Epi_B2AR_GDP_G_ABG_1 0 6.12241161513e-06 0.0905988471091 "" white black 825 -3797 0
simundump kreac /kinetics/Gs/Reac_Gs_BG 0 0.0337380502033 0.0 "" white black 4365 -2079 0
simundump kreac /kinetics/Gs/Reac_GDP_GsA 0 0.00284471758226 0.0 "" white black 6223 -2051 0
simundump kreac /kinetics/Gs/Reac_GDP_G_ABG 0 8.30762162933e-06 0.0 "" white black 5090 -3722 0
simundump kreac /kinetics/cAMP_grp/Reac_GsA_AC1 0 0.000390528083732 1.97859814548 "" white black 8596 -4151 0
simundump kreac /kinetics/Gs/Reac_GTP_GsA_GDP 0 0.000260799655971 0.0 "" white black 5478 -2001 0
simundump kreac /kinetics/Gs/Reac1 0 4.162956189e-07 0.0370021137483 "" white black 1132 -702 0
simundump kreac /kinetics/Gs/Reac_Iso_B2AR_GDP_Gs_ABG 0 7.85904608952e-06 0.105345723162 "" white black 405 -1711 0
simundump kreac /kinetics/cAMP_grp/Reac_GsA_AC2 0 0.000671606501006 1.1703262174 "" white black 10000 -4098 0
simundump kreac /kinetics/PKA/Reac_R2C2 0 8.67392891342e-06 0.0066 "" white black 916 -5916 0
simundump kreac /kinetics/PKA/Reac_cAMP_R2C2 0 1.15652332943e-05 0.0022 "" white black 2443 -5850 0
simundump kreac /kinetics/PKA/Reac_cAMP2_R2C2 0 9.85673740161e-07 0.00075 "" white black 4368 -5918 0
simundump kreac /kinetics/PKA/Reac_cAMP3_R2C2 0 0.000118280847789 0.09 "" white black 5983 -5913 0
simundump kreac /kinetics/PKA/Reac_cAMP4_R2C2 0 59.9999883635 2.83874012212e-11 "" white black 5855 -7500 0
simundump kreac /kinetics/PKA/Reac_cAMP4_R2C 0 59.9999999903 2.83874037157e-11 "" white black 3971 -7539 0
simundump kreac /kinetics/PKA/Reac_PKA_Inhibitor 0 9.46246790009e-05 0.999999999266 "" white black 3020 -7549 0
simundump kreac /kinetics/cAMP_grp/Reac 0 0.1 0.0 "" white black 9960 -480 0
simundump kenz /kinetics/cAMP_grp/cAMP_PDE/PDE 0 0 0 0.0 0 634084.052901 3.80757068837e-06 40.0 10.0 0 0 "" black 4 "" 9374 -1607 0
simundump kenz /kinetics/cAMP_grp/GsA_AC1/ENZ_AC1_GsA 0 0 0 0 0 634084.052901 6.94023994099e-06 70.44298837 17.6107470925 0 1 "" black 7 "" 8859 -2964 0
simundump kenz /kinetics/cAMP_grp/GsA_AC2/ENZ_AC2_GsA 0 0 0 0 0 634084.052901 9.55329209594e-06 95.907309246 23.9768273115 0 1 "" black 52 "" 9653 -2984 0
simundump kenz /kinetics/cAMP_grp/cAMP_PDE_P/ENZ_cAMP_PDE_P 0 0 0 0.0 0 634084.052901 7.83220820635e-06 80.0 20.0 0 0 "" black 23 "" 8984 -676 0
simundump kenz /kinetics/PKA/PKA_Active/Enz_PKA_cAMP_PDE_P 0 0 0 0.0 0 634084.052901 9.32407156107e-06 36.0 9.0 0 0 "" black 49 "" 6592 -7677 0
simundump xgraph /graphs/conc1 0 0 99 0.001 0.999 0
simundump xgraph /graphs/conc2 0 0 100 0 1 0
 simundump xplot /graphs/conc1/_kinetics_0__PKA_0__PKA_Active_0_.conc 3 524288 \
"delete_plot.w <s> <d>; edit_plot.D <w>" black 0 0 1
simundump xplot /graphs/conc1/_kinetics_0__cAMP_grp_0__cAMP_0_.conc 3 524288 \
"delete_plot.w <s> <d>; edit_plot.D <w>" black 0 0 1
simundump xgraph /moregraphs/conc3 0 0 100 0 1 0
simundump xgraph /moregraphs/conc4 0 0 100 0 1 0
 simundump xcoredraw /edit/draw 0 -6 4 -2 6
simundump xtree /edit/draw/tree 0 \
  /kinetics/#[],/kinetics/#[]/#[],/kinetics/#[]/#[]/#[][TYPE!=proto],/kinetics/#[]/#[]/#[][TYPE!=linkinfo]/##[] "edit_elm.D <v>; drag_from_edit.w <d> <S> <x> <y> <z>" auto 0.6
simundump xtext /file/notes 0 1
addmsg /kinetics/Gs/B2AR /kinetics/Gs/Reac_Epi_B2AR SUBSTRATE n 
addmsg /kinetics/Gs/Reac_Epi_B2AR /kinetics/Gs/B2AR REAC A B 
addmsg /kinetics/Gs/Epinephrine /kinetics/Gs/Reac_Epi_B2AR SUBSTRATE n 
addmsg /kinetics/Gs/Reac_Epi_B2AR /kinetics/Gs/Epinephrine REAC A B 
addmsg /kinetics/Gs/Epi_B2AR /kinetics/Gs/Reac_Epi_B2AR PRODUCT n 
addmsg /kinetics/Gs/Reac_Epi_B2AR /kinetics/Gs/Epi_B2AR REAC B A
addmsg /kinetics/Gs/B2AR /kinetics/Gs/Reac_B2AR_GDP_G_ABG SUBSTRATE n 
addmsg /kinetics/Gs/Reac_B2AR_GDP_G_ABG /kinetics/Gs/B2AR REAC A B 
addmsg /kinetics/Gs/GDP_Gs_ABG /kinetics/Gs/Reac_B2AR_GDP_G_ABG SUBSTRATE n 
addmsg /kinetics/Gs/Reac_B2AR_GDP_G_ABG /kinetics/Gs/GDP_Gs_ABG REAC A B 
addmsg /kinetics/Gs/B2AR_GDP_Gs_ABG /kinetics/Gs/Reac_B2AR_GDP_G_ABG PRODUCT n 
addmsg /kinetics/Gs/Reac_B2AR_GDP_G_ABG /kinetics/Gs/B2AR_GDP_Gs_ABG REAC B A
addmsg /kinetics/Gs/GDP_Gs_ABG /kinetics/Gs/Reac_Epi_B2AR_GDP_G_ABG SUBSTRATE n 
addmsg /kinetics/Gs/Reac_Epi_B2AR_GDP_G_ABG /kinetics/Gs/GDP_Gs_ABG REAC A B 
addmsg /kinetics/Gs/Epi_B2AR /kinetics/Gs/Reac_Epi_B2AR_GDP_G_ABG SUBSTRATE n 
addmsg /kinetics/Gs/Reac_Epi_B2AR_GDP_G_ABG /kinetics/Gs/Epi_B2AR REAC A B 
addmsg /kinetics/Gs/Epi_B2AR_GDP_Gs_ABG /kinetics/Gs/Reac_Epi_B2AR_GDP_G_ABG PRODUCT n 
addmsg /kinetics/Gs/Reac_Epi_B2AR_GDP_G_ABG /kinetics/Gs/Epi_B2AR_GDP_Gs_ABG REAC B A
addmsg /kinetics/Gs/B2AR_GDP_Gs_ABG /kinetics/Gs/Reac_Epi_B2AR_GDP_G_ABG_1 SUBSTRATE n 
addmsg /kinetics/Gs/Reac_Epi_B2AR_GDP_G_ABG_1 /kinetics/Gs/B2AR_GDP_Gs_ABG REAC A B 
addmsg /kinetics/Gs/Epinephrine /kinetics/Gs/Reac_Epi_B2AR_GDP_G_ABG_1 SUBSTRATE n 
addmsg /kinetics/Gs/Reac_Epi_B2AR_GDP_G_ABG_1 /kinetics/Gs/Epinephrine REAC A B 
addmsg /kinetics/Gs/Epi_B2AR_GDP_Gs_ABG /kinetics/Gs/Reac_Epi_B2AR_GDP_G_ABG_1 PRODUCT n 
addmsg /kinetics/Gs/Reac_Epi_B2AR_GDP_G_ABG_1 /kinetics/Gs/Epi_B2AR_GDP_Gs_ABG REAC B A
addmsg /kinetics/Gs/Epi_B2AR_GDP_Gs_ABG /kinetics/Gs/Reac_Gs_BG SUBSTRATE n 
addmsg /kinetics/Gs/Reac_Gs_BG /kinetics/Gs/Epi_B2AR_GDP_Gs_ABG REAC A B 
addmsg /kinetics/Gs/GTP_GsA /kinetics/Gs/Reac_Gs_BG PRODUCT n 
addmsg /kinetics/Gs/Reac_Gs_BG /kinetics/Gs/GTP_GsA REAC B A
addmsg /kinetics/Gs/Gs_BG /kinetics/Gs/Reac_Gs_BG PRODUCT n 
addmsg /kinetics/Gs/Reac_Gs_BG /kinetics/Gs/Gs_BG REAC B A
addmsg /kinetics/Gs/Epi_B2AR /kinetics/Gs/Reac_Gs_BG PRODUCT n 
addmsg /kinetics/Gs/Reac_Gs_BG /kinetics/Gs/Epi_B2AR REAC B A
addmsg /kinetics/Gs/GTP_GsA /kinetics/Gs/Reac_GDP_GsA SUBSTRATE n 
addmsg /kinetics/Gs/Reac_GDP_GsA /kinetics/Gs/GTP_GsA REAC A B 
addmsg /kinetics/Gs/GDP_GsA /kinetics/Gs/Reac_GDP_GsA PRODUCT n 
addmsg /kinetics/Gs/Reac_GDP_GsA /kinetics/Gs/GDP_GsA REAC B A
addmsg /kinetics/Gs/Gs_BG /kinetics/Gs/Reac_GDP_G_ABG SUBSTRATE n 
addmsg /kinetics/Gs/Reac_GDP_G_ABG /kinetics/Gs/Gs_BG REAC A B 
addmsg /kinetics/Gs/GDP_GsA /kinetics/Gs/Reac_GDP_G_ABG SUBSTRATE n 
addmsg /kinetics/Gs/Reac_GDP_G_ABG /kinetics/Gs/GDP_GsA REAC A B 
addmsg /kinetics/Gs/GDP_Gs_ABG /kinetics/Gs/Reac_GDP_G_ABG PRODUCT n 
addmsg /kinetics/Gs/Reac_GDP_G_ABG /kinetics/Gs/GDP_Gs_ABG REAC B A
addmsg /kinetics/Gs/GTP_GsA /kinetics/cAMP_grp/Reac_GsA_AC1 SUBSTRATE n 
addmsg /kinetics/cAMP_grp/Reac_GsA_AC1 /kinetics/Gs/GTP_GsA REAC A B 
addmsg /kinetics/cAMP_grp/AC1 /kinetics/cAMP_grp/Reac_GsA_AC1 SUBSTRATE n 
addmsg /kinetics/cAMP_grp/Reac_GsA_AC1 /kinetics/cAMP_grp/AC1 REAC A B 
addmsg /kinetics/cAMP_grp/GsA_AC1 /kinetics/cAMP_grp/Reac_GsA_AC1 PRODUCT n 
addmsg /kinetics/cAMP_grp/Reac_GsA_AC1 /kinetics/cAMP_grp/GsA_AC1 REAC B A
addmsg /kinetics/Gs/GDP_Gs_ABG /kinetics/Gs/Reac_GTP_GsA_GDP SUBSTRATE n 
addmsg /kinetics/Gs/Reac_GTP_GsA_GDP /kinetics/Gs/GDP_Gs_ABG REAC A B 
addmsg /kinetics/Gs/GTP_GsA /kinetics/Gs/Reac_GTP_GsA_GDP PRODUCT n 
addmsg /kinetics/Gs/Reac_GTP_GsA_GDP /kinetics/Gs/GTP_GsA REAC B A
addmsg /kinetics/Gs/Gs_BG /kinetics/Gs/Reac_GTP_GsA_GDP PRODUCT n 
addmsg /kinetics/Gs/Reac_GTP_GsA_GDP /kinetics/Gs/Gs_BG REAC B A
addmsg /kinetics/Gs/B2AR /kinetics/Gs/Reac1 SUBSTRATE n 
addmsg /kinetics/Gs/Reac1 /kinetics/Gs/B2AR REAC A B 
addmsg /kinetics/Gs/Isoproterenol /kinetics/Gs/Reac1 SUBSTRATE n 
addmsg /kinetics/Gs/Reac1 /kinetics/Gs/Isoproterenol REAC A B 
addmsg /kinetics/Gs/Epi_B2AR /kinetics/Gs/Reac1 PRODUCT n 
addmsg /kinetics/Gs/Reac1 /kinetics/Gs/Epi_B2AR REAC B A
addmsg /kinetics/Gs/B2AR_GDP_Gs_ABG /kinetics/Gs/Reac_Iso_B2AR_GDP_Gs_ABG SUBSTRATE n 
addmsg /kinetics/Gs/Reac_Iso_B2AR_GDP_Gs_ABG /kinetics/Gs/B2AR_GDP_Gs_ABG REAC A B 
addmsg /kinetics/Gs/Isoproterenol /kinetics/Gs/Reac_Iso_B2AR_GDP_Gs_ABG SUBSTRATE n 
addmsg /kinetics/Gs/Reac_Iso_B2AR_GDP_Gs_ABG /kinetics/Gs/Isoproterenol REAC A B 
addmsg /kinetics/Gs/Epi_B2AR_GDP_Gs_ABG /kinetics/Gs/Reac_Iso_B2AR_GDP_Gs_ABG PRODUCT n 
addmsg /kinetics/Gs/Reac_Iso_B2AR_GDP_Gs_ABG /kinetics/Gs/Epi_B2AR_GDP_Gs_ABG REAC B A
addmsg /kinetics/Gs/GTP_GsA /kinetics/cAMP_grp/Reac_GsA_AC2 SUBSTRATE n 
addmsg /kinetics/cAMP_grp/Reac_GsA_AC2 /kinetics/Gs/GTP_GsA REAC A B 
addmsg /kinetics/cAMP_grp/AC2 /kinetics/cAMP_grp/Reac_GsA_AC2 SUBSTRATE n 
addmsg /kinetics/cAMP_grp/Reac_GsA_AC2 /kinetics/cAMP_grp/AC2 REAC A B 
addmsg /kinetics/cAMP_grp/GsA_AC2 /kinetics/cAMP_grp/Reac_GsA_AC2 PRODUCT n 
addmsg /kinetics/cAMP_grp/Reac_GsA_AC2 /kinetics/cAMP_grp/GsA_AC2 REAC B A
addmsg /kinetics/PKA/R2C2 /kinetics/PKA/Reac_R2C2 SUBSTRATE n 
addmsg /kinetics/PKA/Reac_R2C2 /kinetics/PKA/R2C2 REAC A B 
addmsg /kinetics/cAMP_grp/cAMP /kinetics/PKA/Reac_R2C2 SUBSTRATE n 
addmsg /kinetics/PKA/Reac_R2C2 /kinetics/cAMP_grp/cAMP REAC A B 
addmsg /kinetics/PKA/cAMP_R2C2 /kinetics/PKA/Reac_R2C2 PRODUCT n 
addmsg /kinetics/PKA/Reac_R2C2 /kinetics/PKA/cAMP_R2C2 REAC B A
addmsg /kinetics/cAMP_grp/cAMP /kinetics/PKA/Reac_cAMP_R2C2 SUBSTRATE n 
addmsg /kinetics/PKA/Reac_cAMP_R2C2 /kinetics/cAMP_grp/cAMP REAC A B 
addmsg /kinetics/PKA/cAMP_R2C2 /kinetics/PKA/Reac_cAMP_R2C2 SUBSTRATE n 
addmsg /kinetics/PKA/Reac_cAMP_R2C2 /kinetics/PKA/cAMP_R2C2 REAC A B 
addmsg /kinetics/PKA/cAMP2_R2C2 /kinetics/PKA/Reac_cAMP_R2C2 PRODUCT n 
addmsg /kinetics/PKA/Reac_cAMP_R2C2 /kinetics/PKA/cAMP2_R2C2 REAC B A
addmsg /kinetics/PKA/cAMP2_R2C2 /kinetics/PKA/Reac_cAMP2_R2C2 SUBSTRATE n 
addmsg /kinetics/PKA/Reac_cAMP2_R2C2 /kinetics/PKA/cAMP2_R2C2 REAC A B 
addmsg /kinetics/cAMP_grp/cAMP /kinetics/PKA/Reac_cAMP2_R2C2 SUBSTRATE n 
addmsg /kinetics/PKA/Reac_cAMP2_R2C2 /kinetics/cAMP_grp/cAMP REAC A B 
addmsg /kinetics/PKA/cAMP3_R2C2 /kinetics/PKA/Reac_cAMP2_R2C2 PRODUCT n 
addmsg /kinetics/PKA/Reac_cAMP2_R2C2 /kinetics/PKA/cAMP3_R2C2 REAC B A
addmsg /kinetics/PKA/cAMP3_R2C2 /kinetics/PKA/Reac_cAMP3_R2C2 SUBSTRATE n 
addmsg /kinetics/PKA/Reac_cAMP3_R2C2 /kinetics/PKA/cAMP3_R2C2 REAC A B 
addmsg /kinetics/cAMP_grp/cAMP /kinetics/PKA/Reac_cAMP3_R2C2 SUBSTRATE n 
addmsg /kinetics/PKA/Reac_cAMP3_R2C2 /kinetics/cAMP_grp/cAMP REAC A B 
addmsg /kinetics/PKA/cAMP4_R2C2 /kinetics/PKA/Reac_cAMP3_R2C2 PRODUCT n 
addmsg /kinetics/PKA/Reac_cAMP3_R2C2 /kinetics/PKA/cAMP4_R2C2 REAC B A
addmsg /kinetics/PKA/cAMP4_R2C2 /kinetics/PKA/Reac_cAMP4_R2C2 SUBSTRATE n 
addmsg /kinetics/PKA/Reac_cAMP4_R2C2 /kinetics/PKA/cAMP4_R2C2 REAC A B 
addmsg /kinetics/PKA/PKA_Active /kinetics/PKA/Reac_cAMP4_R2C2 PRODUCT n 
addmsg /kinetics/PKA/Reac_cAMP4_R2C2 /kinetics/PKA/PKA_Active REAC B A
addmsg /kinetics/PKA/cAMP4_R2C /kinetics/PKA/Reac_cAMP4_R2C2 PRODUCT n 
addmsg /kinetics/PKA/Reac_cAMP4_R2C2 /kinetics/PKA/cAMP4_R2C REAC B A
addmsg /kinetics/PKA/cAMP4_R2C /kinetics/PKA/Reac_cAMP4_R2C SUBSTRATE n 
addmsg /kinetics/PKA/Reac_cAMP4_R2C /kinetics/PKA/cAMP4_R2C REAC A B 
addmsg /kinetics/PKA/cAMP4_R2 /kinetics/PKA/Reac_cAMP4_R2C PRODUCT n 
addmsg /kinetics/PKA/Reac_cAMP4_R2C /kinetics/PKA/cAMP4_R2 REAC B A
addmsg /kinetics/PKA/PKA_Active /kinetics/PKA/Reac_cAMP4_R2C PRODUCT n 
addmsg /kinetics/PKA/Reac_cAMP4_R2C /kinetics/PKA/PKA_Active REAC B A
addmsg /kinetics/PKA/PKA_Inhibitor /kinetics/PKA/Reac_PKA_Inhibitor SUBSTRATE n 
addmsg /kinetics/PKA/Reac_PKA_Inhibitor /kinetics/PKA/PKA_Inhibitor REAC A B 
addmsg /kinetics/PKA/PKA_Active /kinetics/PKA/Reac_PKA_Inhibitor SUBSTRATE n 
addmsg /kinetics/PKA/Reac_PKA_Inhibitor /kinetics/PKA/PKA_Active REAC A B 
addmsg /kinetics/PKA/Inhibited_PKA /kinetics/PKA/Reac_PKA_Inhibitor PRODUCT n 
addmsg /kinetics/PKA/Reac_PKA_Inhibitor /kinetics/PKA/Inhibited_PKA REAC B A
addmsg /kinetics/cAMP_grp/cAMP_PDE_P /kinetics/cAMP_grp/Reac SUBSTRATE n 
addmsg /kinetics/cAMP_grp/Reac /kinetics/cAMP_grp/cAMP_PDE_P REAC A B 
addmsg /kinetics/cAMP_grp/cAMP_PDE /kinetics/cAMP_grp/Reac PRODUCT n 
addmsg /kinetics/cAMP_grp/Reac /kinetics/cAMP_grp/cAMP_PDE REAC B A
addmsg /kinetics/cAMP_grp/cAMP /kinetics/cAMP_grp/cAMP_PDE/PDE SUBSTRATE n 
addmsg /kinetics/cAMP_grp/cAMP_PDE/PDE /kinetics/cAMP_grp/cAMP REAC sA B 
addmsg /kinetics/cAMP_grp/cAMP_PDE/PDE /kinetics/cAMP_grp/AMP MM_PRD pA
addmsg /kinetics/cAMP_grp/cAMP_PDE /kinetics/cAMP_grp/cAMP_PDE/PDE ENZYME n
addmsg /kinetics/cAMP_grp/cAMP_PDE/PDE /kinetics/cAMP_grp/cAMP_PDE REAC eA B
addmsg /kinetics/cAMP_grp/ATP /kinetics/cAMP_grp/GsA_AC1/ENZ_AC1_GsA SUBSTRATE n 
addmsg /kinetics/cAMP_grp/GsA_AC1/ENZ_AC1_GsA /kinetics/cAMP_grp/ATP REAC sA B 
addmsg /kinetics/cAMP_grp/GsA_AC1/ENZ_AC1_GsA /kinetics/cAMP_grp/cAMP MM_PRD pA 
addmsg /kinetics/cAMP_grp/GsA_AC1 /kinetics/cAMP_grp/GsA_AC1/ENZ_AC1_GsA ENZYME n 
addmsg /kinetics/cAMP_grp/ATP /kinetics/cAMP_grp/GsA_AC2/ENZ_AC2_GsA SUBSTRATE n 
addmsg /kinetics/cAMP_grp/GsA_AC2/ENZ_AC2_GsA /kinetics/cAMP_grp/ATP REAC sA B 
addmsg /kinetics/cAMP_grp/GsA_AC2/ENZ_AC2_GsA /kinetics/cAMP_grp/cAMP MM_PRD pA 
addmsg /kinetics/cAMP_grp/GsA_AC2 /kinetics/cAMP_grp/GsA_AC2/ENZ_AC2_GsA ENZYME n 
addmsg /kinetics/cAMP_grp/cAMP /kinetics/cAMP_grp/cAMP_PDE_P/ENZ_cAMP_PDE_P SUBSTRATE n 
addmsg /kinetics/cAMP_grp/cAMP_PDE_P/ENZ_cAMP_PDE_P /kinetics/cAMP_grp/cAMP REAC sA B 
addmsg /kinetics/cAMP_grp/cAMP_PDE_P/ENZ_cAMP_PDE_P /kinetics/cAMP_grp/AMP MM_PRD pA
addmsg /kinetics/cAMP_grp/cAMP_PDE_P /kinetics/cAMP_grp/cAMP_PDE_P/ENZ_cAMP_PDE_P ENZYME n
addmsg /kinetics/cAMP_grp/cAMP_PDE_P/ENZ_cAMP_PDE_P /kinetics/cAMP_grp/cAMP_PDE_P REAC eA B
addmsg /kinetics/cAMP_grp/cAMP_PDE /kinetics/PKA/PKA_Active/Enz_PKA_cAMP_PDE_P SUBSTRATE n 
addmsg /kinetics/PKA/PKA_Active/Enz_PKA_cAMP_PDE_P /kinetics/cAMP_grp/cAMP_PDE REAC sA B 
addmsg /kinetics/PKA/PKA_Active/Enz_PKA_cAMP_PDE_P /kinetics/cAMP_grp/cAMP_PDE_P MM_PRD pA
addmsg /kinetics/PKA/PKA_Active /kinetics/PKA/PKA_Active/Enz_PKA_cAMP_PDE_P ENZYME n
addmsg /kinetics/PKA/PKA_Active/Enz_PKA_cAMP_PDE_P /kinetics/PKA/PKA_Active REAC eA B
addmsg /kinetics/PKA/PKA_Active /graphs/conc1/_kinetics_0__PKA_0__PKA_Active_0_.conc PLOT Co *PKA_Active *26
addmsg /kinetics/cAMP_grp/cAMP /graphs/conc1/_kinetics_0__cAMP_grp_0__cAMP_0_.conc PLOT Co *cAMP *63

enddump
 // End of dump
complete_loading
