from base.fab import *
from plugins.FabFlee.FabFlee import *

@task
def run_ssudan_paper():
  for postfix in ["default","reg","links","ccamp","cborder","redirect","adjumani1","adjumani2"]:  
    #flee("ssudan_%s" % (postfix),simulation_period=604)
    #plot_output("ssudan_%s_localhost_16" % (postfix),"out")

    test_sensitivity("ssudan_%s" % (postfix),simulation_period=604,name="MaxMoveSpeed",values="150-200-250")
    for i in [150, 200, 250]:
      plot_output("ssudan_%s_MaxMoveSpeed_%s_localhost_16" % (postfix, i),"out")

    #test_sensitivity("ssudan_%s" % (postfix),simulation_period=604,name="Awareness",values="0-1-2")
    #for i in [0, 1, 2]:
      #plot_output("ssudan_%s_Awareness_%s_localhost_16" % (postfix, i),"out")



