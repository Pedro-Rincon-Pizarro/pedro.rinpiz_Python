package com.example.listapersonalizada;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;

import java.util.ArrayList;
import java.util.List;

public class MiAdaptadorCiudad extends ArrayAdapter<Ciudad> {
    private Context contexto;
    private int layout;
    private List<Ciudad> arrayCiudades;

    public MiAdaptadorCiudad(@NonNull Context context, int resource, @NonNull List<Ciudad> objects) {
        super(context, resource, objects);
        contexto = context;
        layout = resource;
        arrayCiudades = objects;
    }

    @NonNull
    @Override
    public View getView(int position, @Nullable View convertView, @NonNull ViewGroup parent) {
        View view = LayoutInflater.from(contexto).inflate(layout, parent, false);

        TextView txtNombre = (TextView) view.findViewById(R.id.textView2);
        TextView txtDesc = (TextView) view.findViewById(R.id.textView1);
        ImageView img = (ImageView) view.findViewById(R.id.imageView2);
        Ciudad elemCiudad = arrayCiudades.get(position);
        txtNombre.setText(elemCiudad.getNombre());
        txtDesc.setText(elemCiudad.getDescripcion());
        img.setImageResource(elemCiudad.getImagen());

        return view;
    }
}
