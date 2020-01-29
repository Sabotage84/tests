using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            backgroundWorker1.RunWorkerAsync();
            //progressBar1.BeginInvoke(new Action(() =>
            //{
            //    for (int i = 0; i <= progressBar1.Maximum; i++)
            //    {
            //        
            //    }

            //}
            //)); 
            
        }

        

        private void backgroundWorker1_DoWork(object sender, DoWorkEventArgs e)
        {
            for (int i = 0; i <= 100; i++)
            {
                if (i % 10 == 0)
                {
                    Thread.Sleep(500);
                    backgroundWorker1.ReportProgress(i);
                }
            }
        }

        private void backgroundWorker1_ProgressChanged(object sender, ProgressChangedEventArgs e)
        {
            progressBar1.Value = e.ProgressPercentage;
        }
    }
}
