�
3�,Xc           @   s   d  �  Z  e  d d � GHd S(   c         C   s   |  | S(   N(    (   t   at   b(    (    s4   E:\python\python in hindi\python own program\sum1.pyt   sum1   s    i   i   N(   R   (    (    (    s4   E:\python\python in hindi\python own program\sum1.pyt   <module>   s   	



package "tomcat" do
action :install
only_if { node.default['platform'] = 'CentOS'}
end

service "tomcat" do
  action :restart
end
service "tomcat" do
  action [:enable, :start]
end
