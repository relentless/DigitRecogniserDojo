using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Drawing;

namespace DigitClassifier {
    static class Visualiser {

        const int tileSize = 20;
        const int characerSize = 28;

        public static void Draw( string text, int[] pixels) {

            var form = new Form { TopMost = true, Visible = true, Width = 29 * tileSize, Height = 29 * tileSize };
                 
            var panel = new Panel { Dock = DockStyle.Fill };
            panel.BackColor = Color.Black;

            form.Controls.Add(panel);

            var graphics = panel.CreateGraphics();
        
            for(int index=0; index < pixels.Length; index++){
                int col = index % characerSize;
                int row = index / characerSize;
                Color color = Color.FromArgb(pixels[index], pixels[index], pixels[index]);
                var brush = new SolidBrush(color);
                graphics.FillRectangle(brush,col*tileSize,row*tileSize,tileSize,tileSize);
            }

            var point = new PointF(5, 5);
            var font = new Font(FontFamily.GenericSansSerif, 30 );       
            graphics.DrawString(text, font, new SolidBrush(Color.Red), point);

            Application.EnableVisualStyles();
            Application.Run(form);
        }
    }
}
