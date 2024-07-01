
from flask import current_app, session, flash, redirect, url_for, render_template, request
from models.user import User  
import bcrypt


class UserController:
    def __init__(self, db):
        self.db = db
        self.user_model = User(db)

    def mostrar_datos_usuario(self, user_id):
        user = self.user_model.get_user_by_id(user_id)
        return render_template('views/perfil.html', user=user)
    
    def editar_contraseña(self, request, user_id):
        if request.method == 'POST':
            current_password = request.form.get('current_password')
            new_password = request.form.get('new_password')
            confirm_password = request.form.get('confirm_password')

            if not current_password or not new_password or not confirm_password:
                flash('Todos los campos son requeridos.', 'danger')
                return redirect(url_for('perfil', user_id=user_id))

            # Verificar que la contraseña actual coincida
            user = self.user_model.get_user_by_id(user_id)
            if not user or not bcrypt.checkpw(current_password.encode('utf-8'), user['Password'].encode('utf-8')):
                flash('La contraseña actual es incorrecta.', 'danger')
                return redirect(url_for('perfil', user_id=user_id))

            # Verificar que la nueva contraseña y la confirmación coincidan
            if new_password != confirm_password:
                flash('La nueva contraseña y la confirmación no coinciden.', 'danger')
                return redirect(url_for('perfil', user_id=user_id))

            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())

            success = self.user_model.update_user_password(user_id, hashed_password.decode('utf-8'))

            if success:
                flash('Contraseña actualizada exitosamente.', 'success')
            else:
                flash('Error al actualizar la contraseña.', 'danger')

            return redirect(url_for('perfil', user_id=user_id))

        else:
            return redirect(url_for('perfil', user_id=user_id))